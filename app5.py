import streamlit as st
import os
import hashlib

def hash_file(file_path):
    hasher = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            buf = f.read()
            hasher.update(buf)
        return hasher.hexdigest()
    except Exception:
        return None

def find_duplicates(directory):
    hash_map = {}
    duplicates = []

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = hash_file(file_path)
            if file_hash:
                if file_hash in hash_map:
                    duplicates.append((file_path, hash_map[file_hash]))
                else:
                    hash_map[file_hash] = file_path
    return duplicates

def run(st):
    st.title("🔍 Duplicate File Finder")
    folder_path = st.text_input("Enter the directory to scan:", value=os.path.expanduser("~"))

    if st.button("Find Duplicates"):
        if os.path.exists(folder_path):
            duplicates = find_duplicates(folder_path)
            if duplicates:
                st.write("### Duplicate Files Found:")
                for dup1, dup2 in duplicates:
                    st.write(f"📌 {dup1} ⟷ {dup2}")
            else:
                st.success("No duplicate files found!")
        else:
            st.error("Invalid directory path!")
