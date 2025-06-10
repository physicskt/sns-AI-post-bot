import openai
import os
from dotenv import load_dotenv
import config
# .envファイルを強制的に読み込む
load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_post_text(keyword, sns=None):
    # promptへの指示を取得
    from .sheet import get_prompt_instructions
    instructions = get_prompt_instructions()
    
    # 基本のプロンプトテンプレート
    base_prompt = config.GPT_PROMPT_TEMPLATE.format(char_limit=config.SNS_CHARACTER_LIMIT, keyword=keyword)
    
    # SNS固有の指示がある場合は追加
    if sns and sns in instructions:
        instruction = instructions[sns]
        prompt = f"{base_prompt}。{instruction}。"
    else:
        prompt = base_prompt
    
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