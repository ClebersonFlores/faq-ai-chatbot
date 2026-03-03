from src.vector_store import FAQVectorStore

store = FAQVectorStore()
store.build_index()

print("Index built and saved successfully.")