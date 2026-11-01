from pathlib import path
current_file = path(__file__)
print(current_file)
print(current_file.parent)
print(current_file.parent / "test_files")
