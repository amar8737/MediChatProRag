from langchain_community.vectorstores import Chroma, faiss, FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from typing import List


def create_faiss_index(text:List[str]):
    """ 
    This function return the embedding from text
    """
    embeddings = HuggingFaceEmbeddings(model_name = 'sentance-transformer/all-mpnet-base-v2')
    return FAISS(text,embeddings)

def retrive_relevant_docs(vectorstores:FAISS,query: str,k: int =4):
    """
    """
    return vectorstores.similarity_search(query=query,k=k)

