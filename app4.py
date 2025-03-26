import os
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict
from tqdm import tqdm
import streamlit as st

# Define file categories
FILE_CATEGORIES = {
    "Documents": [".pdf", ".docx", ".txt", ".csv", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executables": [".exe", ".msi", ".bat", ".sh", ".py", ".jar"],
    "System Files": [".sys", ".dll", ".log", ".dat"],
    "Code Files": [".py", ".cpp", ".java", ".js", ".html", ".css"],
    "Others": []
}

# Function to scan drive and count file types
def scan_drive(directory="C:\\", max_files=50000):
    file_count = defaultdict(int)
    file_size = defaultdict(int)
    total_files = 0
    largest_files = []

    for root, _, filenames in tqdm(os.walk(directory), desc="Scanning Drive"):
        for filename in filenames:
            total_files += 1
            file_path = os.path.join(root, filename)
            ext = os.path.splitext(filename)[-1].lower()

            # Determine category
            category = "Others"
            for cat, extensions in FILE_CATEGORIES.items():
                if ext in extensions:
                    category = cat
                    break

            file_count[category] += 1
            try:
                file_size[category] += os.path.getsize(file_path)
                largest_files.append((file_path, os.path.getsize(file_path)))
            except:
                pass  # Ignore inaccessible files

            if total_files >= max_files:  # Stop if max limit reached
                break

    # Sort largest files
    largest_files = sorted(largest_files, key=lambda x: x[1], reverse=True)[:5]
    return file_count, file_size, total_files, largest_files

# Function to generate and save graphs
def plot_file_distribution(file_count, file_size):
    df = pd.DataFrame(list(file_count.items()), columns=["Category", "Count"])
    
    # Pie chart of file count
    plt.figure(figsize=(10, 5))
    plt.pie(df["Count"], labels=df["Category"], autopct="%1.1f%%", startangle=140)
    plt.title("File Type Distribution")
    plt.savefig("file_distribution.png")  # Save pie chart
    plt.close()

    # Bar chart of file sizes
    plt.figure(figsize=(10, 5))
    plt.bar(df["Category"], [file_size[cat] / (1024**3) for cat in df["Category"]], color="skyblue")
    plt.ylabel("Total Size (GB)")
    plt.title("Storage Usage by Category")
    plt.xticks(rotation=45)
    plt.savefig("storage_usage.png")  # Save bar chart
    plt.close()

# ✅ Proper run function for Streamlit
def run(st):
    """Streamlit App for File Scanner"""
    st.title("📂 File Scanner & Analyzer")
    st.write("This tool scans your entire drive and visualizes file distribution.")

    directory = st.text_input("Enter Directory to Scan:", "C:\\Users\\Vansh\\Downloads")

    if st.button("Start Scan", key="file_scan"):
        with st.spinner("🔍 Scanning... Please wait."):
            file_count, file_size, total_files, largest_files = scan_drive(directory)

        # Show results
        st.subheader("📂 Total Files Scanned:")
        st.write(f"**{total_files} files**")

        st.subheader("📊 File Count by Category:")
        for category, count in file_count.items():
            st.write(f"**{category}:** {count} files")

        st.subheader("💾 Top 5 Largest Files:")
        for file, size in largest_files:
            st.write(f"📁 **{file}** - {size / (1024**2):.2f} MB")

        # Generate and show graphs
        plot_file_distribution(file_count, file_size)

        st.subheader("📊 File Distribution Graphs:")
        st.image("file_distribution.png", caption="File Type Distribution")
        st.image("storage_usage.png", caption="Storage Usage by Category")

if __name__ == "__main__":
    run(st)
