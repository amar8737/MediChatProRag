from pypdf import pdf, PdfReader
from typing import List, Optional
from io import BytesIO

def extract_text_from_pdf(file: BytesIO):
    """
    Extract text from each page of a PDF file.

    Args:
        file (BytesIO): A file-like object containing the PDF data.
    returns:
        List[ste]: A list of strings, each representing the text from a page.
    """
    reader = PdfReader(file)
    texts =[] 
    for page in reader.pages:
        texts.append(page.extract_text() or "")
    return texts

