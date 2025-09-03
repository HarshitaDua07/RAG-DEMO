import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import pipeline

# Embedding model
embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Vector DB
dim = 384
index = faiss.IndexFlatL2(dim)
docs = []

# Generator model (lightweight)
generator = pipeline("text2text-generation", model="google/flan-t5-base")

def add_documents(texts):
    global docs
    embeddings = embedder.encode(texts)
    index.add(np.array(embeddings).astype("float32"))
    docs.extend(texts)

def query(question, top_k=3):
    if len(docs) == 0:
        return "No documents available.", []
    q_emb = embedder.encode([question])
    D, I = index.search(np.array(q_emb).astype("float32"), top_k)
    retrieved = [docs[i] for i in I[0] if i < len(docs)]
    context = "\n".join(retrieved)
    prompt = f"Answer the question based only on the context:\n\n{context}\n\nQuestion: {question}\nAnswer:"
    out = generator(prompt, max_new_tokens=200)[0]["generated_text"]
    return out, retrieved
