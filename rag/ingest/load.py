from langchain_community.document_loaders import PyMuPDFLoader
from langchain_core.documents import Document
from pathlib import Path
from rag.config import RAW_DIR


def load_pdfs(raw_dir: Path = RAW_DIR) -> list[Document]:
    loaded_docs: list[Document] = []
    pdf_paths = list(raw_dir.glob("**/*.pdf"))
    for path in pdf_paths:
        doc = PyMuPDFLoader(file_path=path, mode="page").load()
        loaded_docs.extend(doc)

    return loaded_docs
