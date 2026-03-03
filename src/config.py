from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "faq.csv"
INDEX_PATH = BASE_DIR / "models" / "faq_index.faiss"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
TOP_K = 3

# Minimum similarity threshold (0 to 1). Queries below this score
# return a fallback message instead of a wrong answer.
SIMILARITY_THRESHOLD = 0.30