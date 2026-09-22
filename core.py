import os
from dotenv import load_dotenv
from openai import OpenAI

# 加载环境变量
load_dotenv()

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

def analyze_code(code_content, file_name="未知文件"):
    """
    核心逻辑：把代码发给 AI 并返回解释
    """
    response = client.chat.completions.create(
        model="qwen-turbo",
        messages=[
            {"role": "system", "content": "你是一个资深软件工程师，请用简洁易懂的语言解释用户提供的代码。指出它的功能、潜在的Bug以及可以优化的地方。"},
            {"role": "user", "content": f"请解释以下代码文件 {file_name} 的内容：\n\n{code_content}"}
        ]
    )
    return response.choices[0].message.content