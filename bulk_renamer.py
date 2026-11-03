from pathlib import Path


# 1. Get folder path
def get_folder_path():
    current_file = Path(__file__)
    folder_path = current_file.parent / "test_files"
    return folder_path


# 2. Validate folder
def validate_folder(folder_path):
    if not folder_path.exists():
        print("Error: Folder does not exist!")
        return False

    if not folder_path.is_dir():
        print("Error: The given path is not a directory!")
        return False

    return True


# 3. Collect files
def get_files(folder_path):
    files = []

    for item in folder_path.iterdir():
        if item.is_file():
            files.append(item)

    return files


# 4. Get custom naming options
def get_naming_options():
    invalid_chars = '<>:"/\\|?*'

    # Get prefix
    while True:
        prefix = input("Enter a prefix: ").strip()

        if not prefix:
            print("Prefix cannot be empty!")

        elif any(char in invalid_chars for char in prefix):
            print("Prefix contains invalid filename characters!")

        else:
            break

    # Get starting number
    while True:
        start_number = input("Enter starting number: ").strip()

        if start_number.isdigit():
            start_number = int(start_number)
            break

        else:
            print("Please enter a valid positive number!")

    # Get separator
    while True:
        separator = input(
            "Enter separator (_ or - or leave empty): "
        )

        if separator in ("", "_", "-"):
            break

        else:
            print("Please enter only _, -, or leave it empty!")

    return prefix, start_number, separator


# 5. Generate new filenames
def generate_new_names(files, prefix, start_number, separator):
    new_names = []

    for index, file in enumerate(files):
        number = start_number + index

        new_name = (
            f"{prefix}{separator}{number}{file.suffix}"
        )

        new_names.append(new_name)

    return new_names


# 6. Show preview
def show_preview(files, new_names):
    print("\n--- FILE RENAMING PREVIEW ---")

    for old_file, new_file in zip(files, new_names):
        print(f"{old_file.name} -> {new_file}")


# 7. Ask for confirmation
def confirm_renaming():
    while True:
        choice = input(
            "\nDo you want to rename these files? (yes/no): "
        ).strip().lower()

        if choice in ("yes", "no"):
            return choice == "yes"

        print("Invalid choice. Please enter yes or no.")


# 8. Check filename conflicts
def check_conflicts(files, new_names, folder_path):
    files_to_rename = []
    conflicts = []

    for old_file, new_name in zip(files, new_names):
        destination_path = folder_path / new_name

        if old_file == destination_path:
            print(f"Skipping {old_file.name}: Already has intended name.")
        else:
            files_to_rename.append((old_file, destination_path))

    # Check duplicate generated names
    destination_names = [
        destination.name for _, destination in files_to_rename
    ]

    if len(destination_names) != len(set(destination_names)):
        print("\nError: Duplicate filenames generated!")
        return None

    # Check existing destination files
    source_paths = {old_file for old_file, _ in files_to_rename}

    for _, destination_path in files_to_rename:
        if destination_path.exists() and destination_path not in source_paths:
            conflicts.append(destination_path.name)

    if conflicts:
        print("\nFilename conflicts detected!")

        for conflict in conflicts:
            print(f"Already exists: {conflict}")

        return None

    return files_to_rename


# 9. Rename files
def rename_files(files_to_rename):
    success_count = 0
    failed_count = 0

    print("\nStarting file renaming...")

    for old_file, destination_path in files_to_rename:
        try:
            old_name = old_file.name
            old_file.rename(destination_path)

            success_count += 1

            print(f"{old_name} renamed to {destination_path.name}")

        except OSError as error:
            failed_count += 1
            print(f"Could not rename {old_file.name}: {error}")

    return success_count, failed_count


# 10. Show final summary
def show_summary(success_count, failed_count):
    total_files = success_count + failed_count

    print("\n--- RENAMING SUMMARY ---")
    print(f"Total files processed: {total_files}")
    print(f"Successfully renamed: {success_count}")
    print(f"Failed: {failed_count}")

    if failed_count == 0:
        print("\nRenaming completed successfully!")
    else:
        print("\nRenaming completed with errors.")


# 11. Main function
def main():
    print("BULK RENAMER")

    folder_path = get_folder_path()

    if not validate_folder(folder_path):
        return

    try:
        print("\nFolder found successfully!")

        files = get_files(folder_path)

        if not files:
            print("No files found in this folder!")
            return

        print("\nFiles found:")

        for file in files:
            print(file.name)

        print(f"\nTotal files found: {len(files)}")

        prefix, start_number, separator = get_naming_options()

        new_names = generate_new_names(
            files, prefix, start_number, separator
        )

        show_preview(files, new_names)

        if not confirm_renaming():
            print("\nRenaming cancelled!")
            return

        files_to_rename = check_conflicts(
            files, new_names, folder_path
        )

        if files_to_rename is None:
            print("\nNo files were renamed.")
            return

        if not files_to_rename:
            print("\nAll files already have their intended names.")
            return

        success_count, failed_count = rename_files(files_to_rename)

        show_summary(success_count, failed_count)

    except PermissionError:
        print("Error: Permission denied while accessing the folder!")

    except OSError as error:
        print(f"Folder access error: {error}")


# Program execution starts here
if __name__ == "__main__":
    main()