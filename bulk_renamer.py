from pathlib import Path
# Get the current python file location
current_file = Path(__file__)
# Get the test_files folder path
folder_path = current_file.parent / "test_files" 
# Validate the folder path
if folder_path.exists():
    if folder_path.is_dir():
        print("BULK RENAMER")
        print("Folder found successfully!")
    else:
        print("Error: The given path is not a directory!")
else:
    print("Error: Folder does not exist!")
