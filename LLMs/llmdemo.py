from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")   # must match your .env key
)

response = client.chat.completions.create(
    model="meta-llama/llama-3.1-8b-instruct",
    messages=[
        {"role": "user", "content": "What is the capital of America?"}
    ]
)

print(response.choices[0].message.content)
