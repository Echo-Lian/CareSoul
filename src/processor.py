import os
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_chunk_docs(directory_path):
    # Load all PDFs from the clinical data folder
    loader = DirectoryLoader(directory_path, glob="./*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()

    # Use Recursive splitting to keep context together
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        separators=["\n\n", "\n", ".", " "]
    )
    
    chunks = text_splitter.split_documents(documents)
    
    # Example of adding automated metadata for safety/source tracking
    for chunk in chunks:
        chunk.metadata["is_clinical"] = True
        chunk.metadata["processed_at"] = "2023-10-27"
        
    return chunks