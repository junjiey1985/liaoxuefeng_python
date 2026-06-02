from openai import OpenAI

client = OpenAI(
    api_key="sk-2a7f9580bbc942f989151014ea236537",
    base_url="https://api.deepseek.com"  # 如果用DeepSeek
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "将以下内容翻译成英文：今天项目进展顺利，我们完成了核心接口开发。"}]
)

print(response.choices[0].message.content)