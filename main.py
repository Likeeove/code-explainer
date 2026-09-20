import sys
import os
import time
from dotenv import load_dotenv
from openai import OpenAI

# 加载环境变量
load_dotenv()

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 支持的文件后缀
CODE_EXTENSIONS = ('.py', '.cpp', '.java', '.c', '.h', '.js', '.ts')

def analyze_code(code_content, file_name):
    """核心逻辑：调用 AI 解释代码"""
    response = client.chat.completions.create(
        model="qwen-turbo",
        messages=[
            {"role": "system", "content": "你是一个资深软件工程师，请用简洁易懂的语言解释用户提供的代码。指出它的功能、潜在的Bug以及可以优化的地方。"},
            {"role": "user", "content": f"请解释以下代码文件 {file_name} 的内容：\n\n{code_content}"}
        ]
    )
    return response.choices[0].message.content

def explain_file(file_path, output_dir="reports"):
    """处理单个文件，并保存报告"""
    print(f"📄 正在处理：{file_path}")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            code_content = f.read()
        
        # 调用 AI
        ai_result = analyze_code(code_content, os.path.basename(file_path))
        
        # 创建输出目录
        os.makedirs(output_dir, exist_ok=True)
        
        # 保存为 Markdown 文件
        file_name = os.path.basename(file_path)
        report_path = os.path.join(output_dir, f"{file_name}_explain.md")
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(f"# 代码解释：{file_name}\n\n")
            f.write(ai_result)
            
        print(f"✅ 已保存报告：{report_path}")
        return True
    except Exception as e:
        print(f"❌ 处理 {file_path} 时出错：{e}")
        return False

def explain_folder(folder_path):
    """遍历文件夹"""
    if not os.path.isdir(folder_path):
        print(f"❌ 错误：{folder_path} 不是一个有效的文件夹。")
        return

    print(f"📁 开始批量处理文件夹：{folder_path}")
    success_count = 0
    total_count = 0

    # 核心遍历逻辑
    for root, dirs, files in os.walk(folder_path):
        # 过滤掉不需要的文件夹，避免死循环或处理无关文件
        dirs[:] = [d for d in dirs if d not in ['venv', '__pycache__', '.git', 'reports']]
        
        for file in files:
            if file.endswith(CODE_EXTENSIONS):
                total_count += 1
                full_path = os.path.join(root, file)
                
                # 逐个处理，并添加 1 秒延迟，防止请求过快被限流
                if explain_file(full_path):
                    success_count += 1
                time.sleep(1)

    print(f"\n🎉 批量处理完成！共发现 {total_count} 个文件，成功处理 {success_count} 个。")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("💡 用法：python main.py <文件路径或文件夹路径>")
        print("   例如：python main.py test.py")
        print("   例如：python main.py ./my_code")
    else:
        target_path = sys.argv[1]
        if os.path.isdir(target_path):
            explain_folder(target_path)
        else:
            explain_file(target_path)