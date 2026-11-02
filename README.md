Bulk Renamer

A Python-based tool that helps rename multiple files in a folder automatically using a custom prefix, starting number, and separator.

Features

- Automatically detects files inside a selected folder.
- Allows users to enter a custom filename prefix.
- Supports a custom starting number.
- Allows different separators ("_", "-", or none).
- Preserves the original file extensions.
- Displays a preview before renaming.
- Asks for confirmation before renaming files.
- Detects filename conflicts.
- Handles errors during the renaming process.
- Displays a final summary of the operation.

Technologies Used

- Python
- pathlib module
- VS Code
- Git and GitHub

Project Structure

bulk-renamer/
│
├── bulk_renamer.py
├── README.md
├── .gitignore
│
└── test_files/
    ├── cat.jpg
    ├── dog.png
    ├── notes.txt
    └── report.pdf

How to Run

1. Clone this repository:
   
   git clone https://github.com/nainabharti/bulk-renamer.git

2. Open the project folder in VS Code.

3. Run the Python file:
   
   python bulk_renamer.py

4. Enter your preferred prefix, starting number, and separator.

5. Review the filename preview.

6. Confirm the operation to rename the files.

Example

Suppose the folder contains:

cat.jpg
dog.png
notes.txt

With the following options:

- Prefix: "photo"
- Starting number: "1"
- Separator: "_"

The files will be renamed to:

photo_1.jpg
photo_2.png
photo_3.txt

Note

Always keep a backup of important files before performing bulk renaming.