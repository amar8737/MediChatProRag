import streamlit as st

def pdf_uploader():
    return st.file_uploader(
        "Upload PDF files",
        type=["pdf"],
        accept_multiple_files=True,   # <-- allow multiple
        help="Upload one or more PDF files to process."
    )
