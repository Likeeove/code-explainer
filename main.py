import sys
import os
from openai import OpenAI
from dotenv import load_dotenv

# 加载 .env 文件里的环境变量
load_dotenv()

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),  # 自动从 .env 读取
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

def explain_code(file_path):
    # 1. 尝试读取文件
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            code_content = f.read()
    except FileNotFoundError:
        print(f"❌ 找不到文件：{file_path}，请检查路径是否正确。")
        return
    except Exception as e:
        print(f"❌ 读取文件出错：{e}")
        return

    print(f"📄 已读取文件：{file_path}")
    print("🤖 正在请求 AI 解释，请稍等...\n")

    # 2. 把代码发给 AI
    response = client.chat.completions.create(
        model="qwen-turbo",
        messages=[
            {"role": "system", "content": "你是一个资深软件工程师，请用简洁易懂的语言解释用户提供的代码。指出它的功能、潜在的Bug以及可以优化的地方。"},
            {"role": "user", "content": f"请解释这段代码：\n\n{code_content}"}
        ]
    )

    # 3. 打印结果
    print("=" * 40)
    print("✨ AI 解释：")
    print("=" * 40)
    print(response.choices[0].message.content)

if __name__ == "__main__":
    # 检查用户有没有输入文件名
    if len(sys.argv) < 2:
        print("💡 用法：python main.py <代码文件路径>")
        print("   例如：python main.py test.py")
    else:
        explain_code(sys.argv[1])