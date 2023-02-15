import os
import re


def remove_comments(code):
    pattern = r"(^|\s+)#.*"
    code = re.sub(pattern, "", code)
    code = re.sub(r'\n\s*\n', '\n', code)
    return re.sub(pattern, "", code)


def pyOne(file_path):
    if not os.path.isfile(file_path):
        print(f"The file {file_path} was not found.")
        return

    with open(file_path, "r") as f:
        code = f.read()

    code = remove_comments(code)

    with open(file_path, "w") as f:
        f.write(code)

    print(f"Comments have been removed from the file {file_path}.")


def pyAll(directory_path):
    if not os.path.isdir(directory_path):
        print(f"The directory {directory_path} was not found.")
        return

    py_files = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.join(root, file))

    print("Files to be processed:")
    for file_path in py_files:
        print(file_path)
    print()

    for file_path in py_files:

        with open(file_path, "r") as f:
            code = f.read()

        code = remove_comments(code)

        with open(file_path, "w") as f:
            f.write(code)

        print(f"Comments have been removed from the file {file_path}.")

    print("All files were successfully processed.")
