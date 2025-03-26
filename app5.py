import os
import hashlib
import shutil
from collections import defaultdict

# Function to calculate file hash (MD5)
def get_file_hash(file_path):
    try:
        hasher = hashlib.md5()
        with open(file_path, 'rb') as f:
            content = f.read()
            if not content:
                return "EMPTY_FILE"  # Special hash for empty files
            hasher.update(content)
        return hasher.hexdigest()
    except:
        return None  # Return None for inaccessible files

# Function to find duplicate files
def find_duplicates(directory="C:\\Users\\Vansh\\OneDrive\\Desktop\\"):
    hash_map = defaultdict(list)
    file_list = []

    # Collect all files from Desktop
    for root, _, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))

    total_count = len(file_list)
    duplicates = {}

    # Process each file
    for idx, file_path in enumerate(file_list):
        file_hash = get_file_hash(file_path)
        if file_hash:
            hash_map[file_hash].append(file_path)

    # Keep only duplicates (files with the same hash)
    duplicates = {h: paths for h, paths in hash_map.items() if len(paths) > 1}
    return duplicates

# Function to delete file
def delete_file(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        return False
    except Exception as e:
        return False

# Streamlit UI Function
def run(st):
    st.title("🔍 AI-Based Duplicate File Finder")
    st.write("Scanning only your **Desktop folder** for duplicate files.")

    # Initialize session state
    if "duplicates" not in st.session_state:
        st.session_state.duplicates = {}

    if st.button("Start Scan", key="start_scan"):
        st.write("🔍 Scanning Desktop for duplicate files...")

        with st.spinner("Scanning in progress... Please wait"):
            st.session_state.duplicates = find_duplicates()

        st.success("✅ Scan completed!")

    if st.session_state.duplicates:
        total_duplicates = sum(len(v) - 1 for v in st.session_state.duplicates.values())
        st.warning(f"⚠️ Found {total_duplicates} duplicate files!")

        for hash_value, file_list in list(st.session_state.duplicates.items()):
            st.subheader(f"🆔 Duplicate Hash: `{hash_value}`")

            for file_path in file_list:
                col1, col2 = st.columns([4, 1])
                col1.write(f"📄 {file_path}")

                # Delete button with unique key
                if col2.button("🗑️ Delete", key=file_path):
                    success = delete_file(file_path)
                    if success:
                        st.success(f"✅ Deleted: {file_path}")
                        # Remove from session state
                        st.session_state.duplicates[hash_value].remove(file_path)
                        if not st.session_state.duplicates[hash_value]:
                            del st.session_state.duplicates[hash_value]  # Remove empty entries
                        st.rerun()  # ✅ FIXED: Refresh UI without restarting scan
                    else:
                        st.error(f"❌ Failed to delete: {file_path}")
