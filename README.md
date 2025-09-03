# Free RAG Demo (Streamlit + HuggingFace + FAISS)

This is a minimal Retrieval-Augmented Generation (RAG) demo that is **100% free**:
- HuggingFace `sentence-transformers/all-MiniLM-L6-v2` for embeddings
- FAISS for vector search (local, free)
- HuggingFace pipeline (e.g., `google/flan-t5-base`) for answer generation
- Streamlit for frontend UI (deploy free on [Streamlit Cloud](https://streamlit.io/cloud))

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open http://localhost:8501 in your browser.

## Deploy
- Push to GitHub
- Import into Streamlit Cloud
- Done!

## Files
- `rag.py` → Embedding, FAISS index, answer pipeline
- `ingest.py` → Simple script to add docs
- `app.py` → Streamlit chat UI
- `gold.json` → Sample Q/A eval set
