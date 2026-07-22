from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_ROOT / "data" / "raw"
EMBEDDING_MODEL = "sentence-transformers/all-mpnet-base-v2"
