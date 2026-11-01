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
        # Collect all files
        files = []
        for item in folder_path.iterdir():
            if item.is_file():
                files.append(item)
        #Display collected files
        print("\nFiles found:")
        for file in files:
            print(file.name)
        #Display total number of files
        print(f"\nTotal files found: {len(files)}")
    else:
        print("Error: The given path is not a directory!")
else:
    print("Error: Folder does not exist!")
