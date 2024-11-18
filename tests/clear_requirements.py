import os

def remove_requirements_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == 'requirements.txt':
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Removed: {file_path}")

if __name__ == "__main__":
    target_directory = os.getcwd()
    remove_requirements_files(target_directory)
