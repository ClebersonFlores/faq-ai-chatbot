# 🤖 FAQ AI Chatbot

An intelligent FAQ assistant that uses **Sentence Transformers** and **FAISS** to answer questions via semantic search — no keyword matching, no hallucination. Just fast, accurate retrieval from your own FAQ database.

Built with Python, Streamlit, and [UV](https://docs.astral.sh/uv/) for dependency management.

---

## ✨ Features

- 🔍 **Semantic search** — understands meaning, not just keywords
- ⚡ **FAISS vector index** — millisecond search even with thousands of FAQs
- 💾 **Persistent index** — built once, loaded on every restart (no recomputing)
- 🛡️ **Similarity threshold** — returns a fallback message instead of a wrong answer
- 🗂️ **CSV-driven** — update your FAQ by editing a single spreadsheet
- 🎨 **Clean chat UI** — built with Streamlit's native chat components

---

## 🏗️ Project Structure

```
faq-ai-chatbot/
├── app/
│   └── streamlit_app.py     # Streamlit web interface
├── data/
│   └── faq.csv              # Your FAQ database (question, answer)
├── models/
│   ├── faq_index.faiss      # Auto-generated FAISS index (git-ignored)
│   └── faq_index.npz        # Auto-generated metadata  (git-ignored)
├── scripts/
│   └── build_index.py       # Force-rebuild the vector index
├── src/
│   ├── __init__.py
│   ├── config.py            # Paths, model name, and thresholds
│   ├── embeddings.py        # Sentence Transformer helpers
│   └── vector_store.py      # FAISS index build, save, load, and search
├── .gitignore
├── pyproject.toml           # Dependencies managed by UV
├── uv.lock
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- [UV](https://docs.astral.sh/uv/getting-started/installation/) installed

```bash
# Install UV (if you don't have it yet)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/faq-ai-chatbot.git
cd faq-ai-chatbot
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Add your FAQ data

Edit `data/faq.csv` with your own questions and answers:

```csv
question,answer
How long does delivery take?,"Delivery takes 3–5 business days."
How do I request a refund?,"Refunds can be requested within 30 days of purchase."
```

### 4. Build the vector index

```bash
uv run python scripts/build_index.py
```

> This only needs to run once. The index is saved to `models/` and reused automatically on every app restart.

### 5. Run the app

```bash
uv run streamlit run app/streamlit_app.py
```

Open your browser at `http://localhost:8501` 🎉

---

## ⚙️ Configuration

All settings live in `src/config.py`:

| Variable | Default | Description |
|---|---|---|
| `EMBEDDING_MODEL` | `all-MiniLM-L6-v2` | Sentence Transformer model |
| `TOP_K` | `3` | Number of candidates retrieved by FAISS |
| `SIMILARITY_THRESHOLD` | `0.30` | Minimum score to return an answer |
| `DATA_PATH` | `data/faq.csv` | Path to the FAQ spreadsheet |
| `INDEX_PATH` | `models/faq_index.faiss` | Path to the saved FAISS index |

---

## 🧠 How It Works

```
User question
      │
      ▼
Sentence Transformer (all-MiniLM-L6-v2)
      │  encodes question into a 384-dim vector
      ▼
FAISS IndexFlatIP
      │  finds the most similar FAQ question via inner product
      ▼
Similarity score ≥ threshold?
      │
     Yes ──► Return matching answer
      │
      No ──► Return fallback message
```

1. At startup, each FAQ question in `faq.csv` is converted into a dense vector embedding.
2. These vectors are stored in a FAISS index on disk for instant future lookups.
3. When the user types a question, it is embedded with the same model and compared against all FAQ embeddings.
4. The closest match above the similarity threshold is returned as the answer.

---

## 🛠️ Tech Stack

| Technology | Role |
|---|---|
| [Sentence Transformers](https://www.sbert.net/) | Text embedding model |
| [FAISS](https://github.com/facebookresearch/faiss) | Vector similarity search |
| [Streamlit](https://streamlit.io/) | Web interface |
| [Pandas](https://pandas.pydata.org/) | CSV loading and validation |
| [UV](https://docs.astral.sh/uv/) | Fast Python package manager |

---

## 📄 License

MIT License — feel free to use, modify, and distribute.

---

## 🙋 Author

Made by **[Your Name]** · [LinkedIn](https://linkedin.com/in/YOUR_PROFILE) · [GitHub](https://github.com/YOUR_USERNAME)