import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# 加载环境变量
load_dotenv()

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

st.set_page_config(page_title="Code Explainer", page_icon="🤖")

st.title("🤖 Code Explainer")
st.markdown("粘贴你的代码，让 AI 帮你解释、审查 Bug 并给出优化建议。")

# 页面上的输入框
code_input = st.text_area("📄 在这里粘贴你的代码：", height=300)

# 页面上的按钮
if st.button("✨ 开始解释"):
    if not code_input.strip():
        st.warning("请先粘贴代码！")
    else:
        with st.spinner("AI 正在思考中，请稍候..."):
            try:
                response = client.chat.completions.create(
                    model="qwen-turbo",
                    messages=[
                        {"role": "system", "content": "你是一个资深软件工程师，请用简洁易懂的语言解释用户提供的代码。指出它的功能、潜在的Bug以及可以优化的地方。"},
                        {"role": "user", "content": f"请解释这段代码：\n\n{code_input}"}
                    ]
                )
                result = response.choices[0].message.content
                st.success("解释完成！")
                st.markdown(result)
            except Exception as e:
                st.error(f"出错了：{e}")