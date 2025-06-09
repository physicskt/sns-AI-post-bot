import openai
import os
from dotenv import load_dotenv
import config
# .envファイルを強制的に読み込む
load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_post_text(keyword):
    prompt = config.GPT_PROMPT_TEMPLATE.format(char_limit=config.SNS_CHARACTER_LIMIT, keyword=keyword)
    
    response = client.chat.completions.create(
        model=config.OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=config.OPENAI_MAX_TOKENS
    )
    
    return response.choices[0].message.content.strip()


def generate_test():

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    try:
        models = client.models.list()
        print("✅ APIキーは有効です！利用可能なモデル一覧：")
        for m in models.data[:5]:
            print("-", m.id)
    except openai.AuthenticationError as e:
        print("❌ 認証エラー！APIキーが無効かも")
        print(e)


if __name__ == "__main__":
    generate_test()