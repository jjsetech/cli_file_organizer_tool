# Developed by Jeronimo Junior (JJSETECH)
import os
import shutil
import hashlib
import argparse
from collections import defaultdict

# Define file type categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".txt", ".csv"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Code": [".py", ".java", ".js", ".html", ".css", ".cpp", ".c"],
    "Others": []  # Catch-all category
}


def organize_files(directory):
    """Organize files in the given directory into categorized subfolders."""
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return

    # Create category folders if they don't exist
    for category in FILE_CATEGORIES:
        category_path = os.path.join(directory, category)
        os.makedirs(category_path, exist_ok=True)

    # Sort files into categories
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            file_ext = os.path.splitext(filename)[1].lower()

            # Find the appropriate category
            category = next((cat for cat, exts in FILE_CATEGORIES.items() if file_ext in exts), "Others")
            target_path = os.path.join(directory, category, filename)

            # Move the file
            shutil.move(filepath, target_path)
            print(f"Moved: {filename} -> {category}/")


def find_duplicates(directory):
    """Find duplicate files in the given directory based on file hashes."""
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return

    file_hashes = defaultdict(list)

    # Generate hashes for all files
    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_hash = hash_file(filepath)
            file_hashes[file_hash].append(filepath)

    # Identify duplicates
    duplicates = {hash_val: paths for hash_val, paths in file_hashes.items() if len(paths) > 1}
    if not duplicates:
        print("No duplicate files found.")
        return

    # Display duplicates and prompt for deletion
    print("Duplicate files found:")
    for paths in duplicates.values():
        print("\n".join(paths))
        delete = input("Delete these duplicates? (y/n): ").strip().lower()
        if delete == 'y':
            for duplicate in paths[1:]:
                os.remove(duplicate)
                print(f"Deleted: {duplicate}")


def hash_file(filepath, chunk_size=1024):
    """Generate a hash for the given file."""
    hasher = hashlib.md5()
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(chunk_size):
                hasher.update(chunk)
    except Exception as e:
        print(f"Error hashing file {filepath}: {e}")
    return hasher.hexdigest()


def main():
    """Parse command-line arguments and execute the tool."""
    parser = argparse.ArgumentParser(description="CLI File Organizer Tool")
    parser.add_argument("directory", help="Path to the directory to organize")
    parser.add_argument("--find-duplicates", action="store_true", help="Find and optionally remove duplicate files")

    args = parser.parse_args()

    if args.find_duplicates:
        find_duplicates(args.directory)
    else:
        organize_files(args.directory)


if __name__ == "__main__":
    main()
