import os


def ensure_files_and_directories():
    required_paths = {
        "server/data/": "dir",
        "utilities/key.txt": "file",
        "logger/Data_File.txt": "file",
        "server/Full_names.txt": "file",
        "server/log.txt": "file",
        "user/usernames_and_passwords.json": "file"
    }

    for path, path_type in required_paths.items():
        if path_type == "dir":
            if not os.path.exists(path):
                os.makedirs(path)
                print(f"Created directory: {path}")
            else:
                print(f"Directory already exists: {path}")
        elif path_type == "file":
            if not os.path.exists(path):
                with open(path, "w") as f:
                    pass  # Create an empty file
                print(f"Created file: {path}")
            else:
                print(f"File already exists: {path}")


if __name__ == "__main__":
    ensure_files_and_directories()