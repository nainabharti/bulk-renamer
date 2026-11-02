from pathlib import Path

# Step 1: Get the current Python file location
current_file = Path(__file__)

# Step 2: Get the test_files folder path
folder_path = current_file.parent / "test_files"

# Step 3: Validate the folder path
if folder_path.exists():
    if folder_path.is_dir():
        print("BULK RENAMER")
        print("\nFolder found successfully!")

        # Step 4: Collect all files
        files = []

        for item in folder_path.iterdir():
            if item.is_file():
                files.append(item)

        print("\nFiles found:")

        for file in files:
            print(file.name)

        print(f"\nTotal files found: {len(files)}")

        if not files:
            print("No files found in this folder!")

        else:
            # Step 5: Get custom naming options
            print("\n--- CUSTOM NAMING OPTIONS ---")

            while True:
                prefix = input("Enter a prefix: ").strip()

                if prefix:
                    break
                else:
                    print("Prefix cannot be empty. Try again.")

            while True:
                start_number = input("Enter starting number: ").strip()

                if start_number.isdigit():
                    start_number = int(start_number)
                    break
                else:
                    print("Please enter a valid positive number.")

            separator = input("Enter separator (e.g. _ or -): ")

            print("\nNaming options saved successfully!")

            # Step 6: Generate new filenames
            new_names = []

            for index, file in enumerate(files):
                number = start_number + index

                new_name = (
                    f"{prefix}{separator}{number}{file.suffix}"
                )

                new_names.append(new_name)

            # Display filename preview
            print("\n--- FILE RENAMING PREVIEW ---")

            for old_file, new_file in zip(files, new_names):
                print(f"{old_file.name} -> {new_file}")

            # Step 7: Ask for user confirmation
            while True:
                choice = input(
                    "\nDo you want to rename these files? (yes/no): "
                ).strip().lower()

                if choice in ("yes", "no"):
                    break
                else:
                    print("Invalid choice. Please enter yes or no.")

            if choice == "yes":

                # Step 9: Check for filename conflicts
                destination_paths = []

                for new_name in new_names:
                    destination_path = folder_path / new_name
                    destination_paths.append(destination_path)

                conflicts = []

                # Check whether destination files already exist
                for destination_path in destination_paths:
                    if destination_path.exists():
                        conflicts.append(destination_path.name)

                # Check for duplicate generated filenames
                if len(new_names) != len(set(new_names)):
                    print("\nError: Duplicate filenames generated!")

                elif conflicts:
                    print("\nFilename conflicts detected!")

                    for conflict in conflicts:
                        print(f"Already exists: {conflict}")

                    print("\nNo files were renamed.")

                else:
                    # Step 10: Initialize counters
                    success_count = 0
                    failed_count = 0

                    print("\nStarting file renaming...")

                    # Step 8: Rename files with error handling
                    for old_file, destination_path in zip(
                        files, destination_paths
                    ):
                        try:
                            old_file.rename(destination_path)

                            success_count += 1

                            print(
                                f"{old_file.name} renamed to "
                                f"{destination_path.name}"
                            )

                        except OSError as error:
                            failed_count += 1

                            print(
                                f"Could not rename {old_file.name}: "
                                f"{error}"
                            )

                    # Step 10: Display final summary
                    total_files = success_count + failed_count

                    print("\n--- RENAMING SUMMARY ---")
                    print(f"Total files processed: {total_files}")
                    print(f"Successfully renamed: {success_count}")
                    print(f"Failed: {failed_count}")

                    if failed_count == 0:
                        print("\nRenaming operation completed successfully!")
                    else:
                        print("\nRenaming operation completed with errors.")

            else:
                print("\nRenaming cancelled!")

    else:
        print("Error: The given path is not a directory!")

else:
    print("Error: Folder does not exist!")