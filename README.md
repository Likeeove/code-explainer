# Code Explainer (基于 AI 的代码解释 CLI 工具)

一个用 Python 编写的命令行工具，调用阿里云百炼（通义千问）API，自动解释本地代码文件，并给出潜在 Bug 和优化建议。

## ✨ 功能特点

- 读取本地代码文件，自动识别语言
- 调用 LLM 进行解释、审查 Bug、提供优化建议
- 保护 API Key，使用 `.env` 管理密钥

## 🚀 快速开始

### 1. 克隆项目并安装依赖
\`\`\`bash
git clone https://github.com/Likeeove/code-explainer.git
cd code-explainer
pip install openai python-dotenv
\`\`\`

### 2. 配置环境变量
在项目根目录新建 `.env` 文件，填入你的 API Key：
\`\`\`text
DASHSCOPE_API_KEY=sk-ws-H.PHRELDH.YzG1.MEUCIQC51oUWPa0qApkFaQA0POXPFcroJL-dCwZ_QmrnCYc4-gIgTTR9WkzpvMz_ghHLmUEw8ainCJ6Ff9oI9hPsjP-ZXzU
\`\`\`

### 3. 运行工具
\`\`\`bash
python main.py test.py
\`\`\`

## 🛠️ 技术栈
- Python 3
- OpenAI SDK
- 阿里云百炼 (qwen-turbo)

## 📝 后续计划
- [ ] 支持批量处理文件夹
- [ ] 增加 Web 界面
- [ ] 加入 Git Hook 自动审查