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
        #Get custom naming options
        print("\n---CUSTOM NAMING OPTIONS---")
        #Get prefix
        while True:
            prefix = input("Enter a prefix: ").strip()
            if prefix:
                break
            else:
                print("Prefix cannot be empty. Try again.")
        #Get starting number
        while True:
            start_number = input("Enter starting number: ").strip()
            if start_number.isdigit():
                start_number = int(start_number)
                break
            else:
                print("Please enter a valid positive number .")
        #Get separator
        separator = input("Enter separator (e.g. _ or -): ")
        #Display selected options
        print("\n--- YOUR NAMING OPTIONS ---")
        print(f"Prefix: {prefix}")
        print(f"Starting number: {start_number}")
        print(f"Separator: {separator}")
        print("\nNaming options saved successfully!")
        #generate new filenames
        new_names = []
        for index, file in enumerate(files):
            #generate the new number
            number = start_number + index
            #generate new filename
            new_name = f"{prefix}{separator}{number}{file.suffix}"
            #store new filename 
            new_names.append(new_name)
        #display filename preview
        print("\n--- FILE RENAMING PREVIEW ---")
        for old_file, new_file in zip(files, new_names):
            print(f"{old_file.name} -> {new_file}")
    else:
        print("Error: The given path is not a directory!")
else:
    print("Error: Folder does not exist!")
