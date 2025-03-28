import streamlit as st
import os
import numpy as np

def run(st):
    st.title("📂 AI File Manager")
    folder_path = st.text_input("Enter the folder path:", value=os.path.expanduser("~"))

    if st.button("List Files"):
        if os.path.exists(folder_path):
            files = os.listdir(folder_path)
            for file in files:
                st.write(file)
        else:
            st.error("Invalid folder path!")

    st.write("Select a file to manage:")
    selected_file = st.text_input("Enter filename to open:")
    
    if st.button("Open File"):
        file_path = os.path.join(folder_path, selected_file)
        if os.path.exists(file_path):
            os.system(f'open "{file_path}"' if os.name == 'posix' else f'start "" "{file_path}"')
            st.success(f"Opening {selected_file}...")
        else:
            st.error("File not found!")
