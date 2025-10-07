import os

def search_string_in_files(root_dir, search_string):
    for foldername, subfolders, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".py"):  # search only Python files
                file_path = os.path.join(foldername, filename)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        for i, line in enumerate(f, start=1):
                            if search_string in line:
                                print(f"Found in {file_path}, line {i}: {line.strip()}")
                except Exception as e:
                    print(f"Could not read {file_path}: {e}")

if __name__ == "__main__":
    search_string_in_files("Scripts", search_string ="Checking PB switch with mode n")

