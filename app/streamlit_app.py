import sys
import os

# Ensure project root is in sys.path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import streamlit as st
from src.vector_store import FAQVectorStore

# Cache to avoid reloading the model every run
@st.cache_resource
def load_store():
    return FAQVectorStore()

store = load_store()

# Streamlit UI
st.title("🤖 AI-Powered FAQ Assistant")
st.markdown("Ask questions about our services and get instant answers.")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Type your question here")

if user_input:
    answer = store.search(user_input)
    st.session_state.history.append((user_input, answer))

for q, a in reversed(st.session_state.history):
    st.markdown(f"**Q:** {q}")
    st.markdown(f"**A:** {a}")
    st.markdown("---")
