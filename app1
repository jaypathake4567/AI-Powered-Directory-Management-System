import os
import streamlit as st

def search_files(directory, query):
    """Search for files containing the query in the given directory."""
    results = []
    if not os.path.exists(directory):
        return None  # Return None if directory doesn't exist

    for root, _, files in os.walk(directory):
        for file in files:
            if query.lower() in file.lower():
                results.append(os.path.join(root, file))
    return results

def run():
    """Streamlit UI to search for files."""
    st.title("🔍 Search File by Name")
    
    query = st.text_input("Enter file name or keyword:")
    directory = st.text_input("Enter directory to search in:", "C:\\Users\\Vansh\\Downloads")  # Default to Downloads

    if st.button("Search"):
        with st.spinner("🔍 Searching... Please wait."):
            results = search_files(directory, query)

        if results is None:
            st.warning("⚠️ Directory does not exist! Please enter a valid path.")
        elif results:
            st.write("### Search Results:")
            for file in results:
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.write(f"📄 {file}")
                with col2:
                    if st.button("📂 Open", key=file+"open"):
                        os.startfile(file)
        else:
            st.warning("No matching files found!")

if __name__ == "__main__":
    run()
