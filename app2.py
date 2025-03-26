import streamlit as st
import os

def search_files(directory, query):
    results = []
    for root, _, files in os.walk(directory):
        for file in files:
            if query.lower() in file.lower():
                results.append(os.path.join(root, file))
    return results

def run(st):
    st.title("🔍 AI-Powered File Search")
    folder_path = st.text_input("Enter the directory path:", value=os.path.expanduser("~"))
    query = st.text_input("Enter search query:")

    if st.button("Search"):
        if os.path.exists(folder_path):
            results = search_files(folder_path, query)
            if results:
                st.write("### Search Results:")
                for file in results:
                    st.write(file)
            else:
                st.warning("No matching files found.")
        else:
            st.error("Invalid directory path!")
