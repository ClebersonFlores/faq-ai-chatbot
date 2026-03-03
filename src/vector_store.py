import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

TOP_K = 1  # number of top answers to return

class FAQVectorStore:
    def __init__(self):
        # Initialize the model
        self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

        # Sample FAQ dataset (replace with your own)
        self.df = [
            {"question": "What are your working hours?", "answer": "Our working hours are from 9 AM to 6 PM."},
            {"question": "How can I contact you?", "answer": "You can send an email to contact@company.com."},
            {"question": "What services do you offer?", "answer": "We offer consulting, support, and training."},
        ]

        # Build FAISS index
        self.build_index()

    def build_index(self):
        questions = [item["question"] for item in self.df]
        embeddings = self.model.encode(questions, convert_to_numpy=True, normalize_embeddings=True)
        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings.astype("float32"))  # FAISS requires float32

        # Save questions and answers for retrieval
        self.questions = questions
        self.answers = [item["answer"] for item in self.df]

        print(f"✅ FAISS index created with {len(self.df)} questions.")

    def search(self, query, top_k=TOP_K):
        query_embedding = self.model.encode([query], convert_to_numpy=True, normalize_embeddings=True)
        D, I = self.index.search(query_embedding.astype("float32"), top_k)
        idx = I[0][0]
        return self.answers[idx]
