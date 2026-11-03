Bulk Renamer

A Python-based command-line tool that automatically renames multiple files in a folder using a custom prefix, starting number, and separator.

The project is built using modular programming, with separate functions for different tasks, making the code easier to understand, maintain, and reuse.

Features

- Automatically detects files inside a folder.
- Allows users to enter a custom filename prefix.
- Supports a custom starting number.
- Allows different separators ("_", "-", or none).
- Preserves the original file extensions.
- Displays a preview before renaming files.
- Asks for user confirmation before renaming.
- Detects duplicate generated filenames.
- Checks for existing filename conflicts.
- Handles errors during the renaming process.
- Displays a final summary of the operation.
- Uses modular programming with reusable functions.
- Includes input validation and exception handling.

Technologies Used

- Python – Core programming language.
- pathlib – For handling file and folder paths.
- Git – Version control.
- GitHub – Project hosting.

Python Concepts Used

- Functions and modular programming
- Lists and loops
- Conditional statements
- String formatting (f-strings)
- "enumerate()" and "zip()"
- List comprehensions
- Sets
- File and folder handling
- Exception handling ("try-except")
- User input and validation
- "__name__ == "__main__""

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

1. Clone the repository

git clone https://github.com/nainabharti/bulk-renamer.git

2. Open the project folder

Open the cloned folder in VS Code.

3. Run the Python file

python bulk_renamer.py

4. Enter naming options

Provide the following inputs:

- Prefix
- Starting number
- Separator ("_", "-", or empty)

5. Preview and confirm

Review the new filenames and confirm the operation when prompted.

Example

Suppose the folder contains:

cat.jpg
dog.png
notes.txt

Enter the following options:

Option| Value
Prefix| photo
Starting number| 1
Separator| _

Expected output

photo_1.jpg
photo_2.png
photo_3.txt

The original file extensions are preserved.

Modular Program Structure

The project is divided into separate functions, where each function performs a specific task.

Function| Responsibility
"get_folder_path()"| Gets the folder path.
"validate_folder()"| Validates the folder.
"get_files()"| Collects files from the folder.
"get_naming_options()"| Takes custom naming options.
"generate_new_names()"| Generates new filenames.
"show_preview()"| Displays the renaming preview.
"confirm_renaming()"| Gets user confirmation.
"check_conflicts()"| Checks filename conflicts.
"rename_files()"| Renames the files.
"show_summary()"| Displays the final summary.
"main()"| Controls the complete program.

Important Note

Always keep a backup of important files before performing bulk renaming. Test the program with sample files before using it on important folders.

Author

Naina Bharti

GitHub: "@nainabharti" (https://github.com/nainabharti)