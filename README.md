# CLI File Organizer Tool

## Description
The **CLI File Organizer Tool** is a Python script designed to help users efficiently manage and organize files within a directory. It can automatically sort files into categorized subfolders (e.g., `Images`, `Documents`, `Videos`) and detect duplicate files, providing an option to remove them. This tool is ideal for users looking to declutter their file systems and manage directories with ease.

---

## Features
- **Organize Files by Type**: Automatically moves files into categorized subfolders based on their extensions (e.g., `.jpg` to `Images/`).
- **Duplicate Detection**: Finds duplicate files using hash comparison and allows users to delete them interactively.
- **Command-Line Interface**: Simple and intuitive CLI for seamless usage.
- **Extensible Categories**: Easily add or modify file type categories in the `FILE_CATEGORIES` dictionary.

---

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/jjsetech/cli_file_organizer_tool.git
   ```

2. Navigate to the project directory:
   ```bash
   cd cli_file_organizer_tool
   ```

3. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install dependencies (if any). The script uses only standard Python libraries.

---

## Usage
Run the script using Python from the command line. Below are the available options:

### Organize Files
Organize files in a specified directory:
```bash
python file_organizer.py /path/to/directory # Change /path/to/directory for your directory you want to organize. Example: C:\MiscFiles
```

### Find and Remove Duplicate Files
Find duplicate files in a directory and optionally delete them:
```bash
python file_organizer.py /path/to/directory --find-duplicates # Change /path/to/directory for your directory you want to search for duplicates. Example: C:\MiscFiles
```

---

## Example
### Before
```
/path/to/directory
├── photo1.jpg
├── document.pdf
├── video.mp4
├── duplicate.jpg
├── duplicate.jpg (duplicate)
```

### After (Organized)
```
/path/to/directory
├── Images
│   ├── photo1.jpg
│   └── duplicate.jpg
├── Documents
│   └── document.pdf
├── Videos
│   └── video.mp4
├── Others
```

---

## Configuration
To customize file type categories, edit the `FILE_CATEGORIES` dictionary in `file_organizer.py`:
```python
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".doc", ".docx"],
    "Videos": [".mp4", ".mkv"],
    "Others": []  # Catch-all category
}
```

---

## Contributions
Contributions are welcome! If you have suggestions for new features or improvements, feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch for your feature/fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature/fix"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Author
[Jeronimo Junior](https://github.com/jjsetech)

