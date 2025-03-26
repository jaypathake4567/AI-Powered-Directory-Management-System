import streamlit as st
import os

def scan_files(directory):
    all_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            all_files.append(os.path.join(root, file))
    return all_files

def run(st):
    st.title("📂 Full System File Scanner")
    folder_path = st.text_input("Enter the directory to scan:", value=os.path.expanduser("~"))

    if st.button("Scan"):
        if os.path.exists(folder_path):
            files = scan_files(folder_path)
            st.write(f"### Found {len(files)} files:")
            for file in files[:50]:  # Show first 50 files
                st.write(file)
        else:
            st.error("Invalid directory path!")
