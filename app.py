import streamlit as st
from core import analyze_code # 引入核心逻辑

st.set_page_config(page_title="Code Explainer", page_icon="🤖")
st.title("🤖 Code Explainer")
st.markdown("粘贴你的代码，让 AI 帮你解释、审查 Bug 并给出优化建议。")

code_input = st.text_area("📄 在这里粘贴你的代码：", height=300)

if st.button("✨ 开始解释"):
    if not code_input.strip():
        st.warning("请先粘贴代码！")
    else:
        with st.spinner("AI 正在思考中，请稍候..."):
            try:
                # 直接调用 core.py 里的函数
                result = analyze_code(code_input, file_name="网页粘贴的代码")
                st.success("解释完成！")
                st.markdown(result)
            except Exception as e:
                st.error(f"出错了：{e}")