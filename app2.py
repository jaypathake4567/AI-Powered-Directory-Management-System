import os
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_all_files(directory, max_files=1000):
    """Retrieve all file names in the directory (up to max_files)."""
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.join(root, filename))
            if len(files) >= max_files:
                return files
    return files

def ai_search(files, query):
    """AI-powered file search using TF-IDF + Cosine Similarity."""
    vectorizer = TfidfVectorizer()
    file_names = [os.path.basename(file) for file in files]  # Extract only file names
    
    corpus = file_names + [query]  # Include query
    tfidf_matrix = vectorizer.fit_transform(corpus)
    
    query_vector = tfidf_matrix[-1]  # Last entry is the query
    similarities = cosine_similarity(query_vector, tfidf_matrix[:-1])  # Compare query with files
    
    ranked_files = sorted(zip(files, similarities[0]), key=lambda x: x[1], reverse=True)
    return [file for file, score in ranked_files if score > 0.1]  # Filter results with score > 0.1

def run():
    """Streamlit UI for AI-Powered NLP File Search."""
    st.title("🤖 AI-Powered File Search (NLP)")

    query = st.text_input("Describe the file:")
    directory = st.text_input("Enter directory:", "C:\\Users\\Vansh\\Downloads")

    if st.button("Find File"):
        with st.spinner("🔍 Searching... Please wait."):
            files = get_all_files(directory)
            results = ai_search(files, query)

        if results:
            st.write("### Search Results:")
            for file in results:
                st.write(f"📄 {file}")
        else:
            st.warning("No relevant files found!")

if __name__ == "__main__":
    run()
