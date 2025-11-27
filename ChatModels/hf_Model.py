from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    task="text-generation",
    max_new_tokens=10,
    huggingfacehub_api_token=os.getenv("HF_API_KEY"),
)

chat = ChatHuggingFace(llm=llm)

response = chat.invoke("What is the capital of America?")
print(response.content)
