
from langchain_huggingface import HuggingFaceEmbeddings

####GOnnna download machine on your RAM
embeddings = HuggingFaceEmbeddings(
     model_name="sentence-transformers/all-MiniLM-L6-v2",   
   )
text = "this is test."
query_result = embeddings.embed_query(text)
print(str(query_result))