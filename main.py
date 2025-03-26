import streamlit as st

st.set_page_config(page_title="AI-Powered Directory Manager", page_icon="📂", layout="wide")

st.sidebar.title("🔍 Navigation")
selected_page = st.sidebar.radio(
    "Select a feature:",
    ["Home", "Search File by Name", "Search File with NLP", "Summarize Files", "File Scanner", "Duplicate Finder"]
)

if selected_page == "Home":
    st.title("📂 AI-Powered Directory Manager")
    st.write("Welcome! Use the sidebar to navigate.")

elif selected_page == "Search File by Name":
    import app
    app.run()

elif selected_page == "Search File with NLP":
    import app2
    app2.run()

elif selected_page == "Summarize Files":
    import app3
    app3.run()

elif selected_page == "File Scanner":
    import app4
    app4.run(st)

elif selected_page == "Duplicate Finder":
    import app5
    app5.run(st)
