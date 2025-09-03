import streamlit as st
from rag import add_documents, query

st.title("Free RAG Demo (HuggingFace + FAISS)")

st.markdown("### Upload / Paste")
doc = st.text_area("Paste text to add to knowledge base")
if st.button("Ingest"):
    if doc.strip():
        add_documents([doc.strip()])
        st.success("Document added!")
    else:
        st.warning("Please paste some text first.")

st.markdown("### Ask a Question")
q = st.text_input("Enter your question")
if st.button("Query"):
    if q.strip():
        answer, ctx = query(q.strip())
        st.subheader("Answer")
        st.write(answer)
        st.subheader("Sources")
        for c in ctx:
            st.write("-", c)
    else:
        st.warning("Please enter a question.")
