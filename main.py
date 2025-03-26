import streamlit as st
import app  # Main File Manager
import app2  # AI Search System
import app3  # File Summarizer
import app4  # File Scanner
import app5  # Duplicate Finder

st.set_page_config(page_title="AI File Manager", layout="wide")

# Sidebar Navigation
selected_page = st.sidebar.radio(
    "📌 Select a Tool",
    ["Home", "File Manager", "AI Search System", "File Summarizer", "File Scanner", "Duplicate Finder"]
)

if selected_page == "Home":
    st.title("📂 AI-Powered File Management Suite")
    st.write("Welcome to the AI-powered file management system. Choose a tool from the sidebar.")

elif selected_page == "File Manager":
    app.run(st)  # Main File Manager

elif selected_page == "AI Search System":
    app2.run(st)  # AI Search System

elif selected_page == "File Summarizer":
    app3.run(st)  # File Summarizer

elif selected_page == "File Scanner":
    app4.run(st)  # File Scanner

elif selected_page == "Duplicate Finder":
    app5.run(st)  # Duplicate Finder
