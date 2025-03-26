import os
import streamlit as st
import fitz  # PyMuPDF for PDFs
from docx import Document
import pandas as pd

def extract_text(file_path):
    """Extract text from different file types."""
    try:
        if file_path.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()
        elif file_path.endswith(".pdf"):
            doc = fitz.open(file_path)
            return " ".join([page.get_text() for page in doc])
        elif file_path.endswith(".docx"):
            doc = Document(file_path)
            return " ".join([para.text for para in doc.paragraphs])
        elif file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
            return df.to_string()
        else:
            return "Unsupported file type"
    except Exception as e:
        return f"Error reading file: {e}"

def summarize_text(text, max_words=100):
    """Basic text summarization (extracts first few words)."""
    words = text.split()
    return " ".join(words[:max_words])

def run():
    """Streamlit UI for File Summarization."""
    st.title("📄 File Summarizer")

    uploaded_file = st.file_uploader("Upload a text file:", type=["txt", "docx", "csv", "pdf"])
    if uploaded_file:
        with st.spinner("📄 Processing file..."):
            file_path = f"temp/{uploaded_file.name}"
            with open(file_path, "wb") as f:
                f.write(uploaded_file.read())

            text = extract_text(file_path)
            summary = summarize_text(text)

            st.write("### Summary:")
            st.write(summary)

if __name__ == "__main__":
    run()
