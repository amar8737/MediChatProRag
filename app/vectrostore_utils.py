from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document
from typing import List

def create_faiss_index(chunks: List[str]):
    """
    Create a FAISS vectorstore from a list of text chunks.
    """
    # Convert each chunk into a Document
    documents = [Document(page_content=chunk) for chunk in chunks]

    # Initialize embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2"
    )

    # Create FAISS index from documents
    vectorstore = FAISS.from_documents(documents, embeddings)

    return vectorstore

def retrive_relevant_docs(vectorstore: FAISS, query: str, k: int = 4):
    """
    Retrieve top-k relevant documents from FAISS vectorstore.
    """
    return vectorstore.similarity_search(query=query, k=k)
