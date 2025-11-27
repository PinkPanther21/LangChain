from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",   # or any embedding model OpenRouter supports
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

vec = embeddings.embed_query("Hello, how are you?")
print("Embedding length:", len(vec))
print(vec[:10])
