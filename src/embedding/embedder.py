from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def generate_embedding(data):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(data, embeddings)
    return vectorstore