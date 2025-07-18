import requests
from utils.config import get_together_api_key

MODEL = "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free"

def ai_writer(text):
    API_KEY = get_together_api_key()

    if not API_KEY:
        raise ValueError("TOGETHER_API_KEY not found in .env")

    response = requests.post(
        "https://api.together.xyz/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": MODEL,
            "messages": [{"role": "user", "content": f"Rewrite this chapter:\n\n{text}"}],
            "max_tokens": 1024,
            "temperature": 0.7
        }
    )

    data = response.json()
    return data['choices'][0]['message']['content']