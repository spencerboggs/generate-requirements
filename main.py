import os
import sys
import ast

STANDARD_LIBRARIES = {
    "os", "sys", "platform", "subprocess", "tkinter", 
    "collections", "time", "math", "functools", "itertools", "json", 
    "re", "sqlite3", "pickle", "copy", "argparse", "shutil", "logging", 
    "hashlib", "uuid", "socket", "email", "http", "xml", "unittest", "http.client"
}

def find_imports_in_file(file_path, include_standard):
    imports = set()
    with open(file_path, 'r') as file:
        tree = ast.parse(file.read(), filename=file_path)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.add(alias.name)
            elif isinstance(node, ast.ImportFrom):
                imports.add(node.module)
    if not include_standard:
        imports = {imp for imp in imports if imp not in STANDARD_LIBRARIES}
    return imports

def generate_requirements_for_folder(folder_path, include_standard):
    all_imports = set()
    for root, dirs, files in os.walk(folder_path):
        folder_imports = set()
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                imports = find_imports_in_file(file_path, include_standard)
                folder_imports.update(imports)
        all_imports.update(folder_imports)
    
    if not recursive:
        requirements_file = os.path.join(folder_path, 'requirements.txt')
        with open(requirements_file, 'w') as req_file:
            for import_name in sorted(all_imports):
                req_file.write(f"{import_name}\n")
        print(f"requirements.txt has been generated in {folder_path}")
    else:
        for root, dirs, files in os.walk(folder_path):
            folder_imports = set()
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    imports = find_imports_in_file(file_path, include_standard)
                    folder_imports.update(imports)

            if folder_imports:
                requirements_file = os.path.join(root, 'requirements.txt')
                with open(requirements_file, 'w') as req_file:
                    for import_name in sorted(folder_imports):
                        req_file.write(f"{import_name}\n")
                print(f"requirements.txt has been generated in {root}")

def generate_requirements(directory, include_standard, recursive=False):
    if recursive:
        generate_requirements_for_folder(directory, include_standard)
    else:
        generate_requirements_for_folder(directory, include_standard)

if __name__ == "__main__":
    include_standard = False
    recursive = False
    target_directory = os.getcwd()

    for arg in sys.argv[1:]:
        if arg == "-a":
            include_standard = True
        elif arg == "-r":
            recursive = True
        elif os.path.isdir(arg):
            target_directory = arg
    
    if os.path.isdir(target_directory):
        generate_requirements(target_directory, include_standard, recursive)
    else:
        print(f"Error: The specified directory '{target_directory}' does not exist.")
