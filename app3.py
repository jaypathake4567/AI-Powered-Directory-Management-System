import streamlit as st
import os
import docx
import PyPDF2
from transformers import pipeline

summarizer = pipeline("summarization")

def summarize_text(text):
    return summarizer(text, max_length=150, min_length=50, do_sample=False)[0]['summary_text']

def read_file(file_path):
    if file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    elif file_path.endswith(".pdf"):
        with open(file_path, "rb") as f:
            pdf_reader = PyPDF2.PdfReader(f)
            return "\n".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
    return ""

def run(st):
    st.title("📝 AI-Powered File Summarizer")
    uploaded_file = st.file_uploader("Upload a text, PDF, or DOCX file", type=["txt", "pdf", "docx"])

    if uploaded_file:
        file_text = read_file(uploaded_file.name)
        if file_text:
            st.write("### Original Text:")
            st.text_area("", file_text[:2000], height=300)  # Show first 2000 characters
            
            if st.button("Summarize"):
                summary = summarize_text(file_text)
                st.success("### Summary:")
                st.write(summary)
        else:
            st.error("Could not read file content.")
