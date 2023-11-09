import os
import shutil
from concurrent.futures import ThreadPoolExecutor


def process_folder(folder_path):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    file_extensions = set(os.path.splitext(file)[1] for file in files)

    for ext in file_extensions:
        ext_folder = os.path.join(folder_path, ext[1:])
        os.makedirs(ext_folder, exist_ok=True)

        ext_files = [f for f in files if os.path.splitext(f)[1] == ext]

        with ThreadPoolExecutor() as executor:
            executor.map(move_file, ext_files, [ext_folder] * len(ext_files))


def move_file(file, destination_folder):
    source_path = os.path.join(folder_path, file)
    destination_path = os.path.join(destination_folder, file)
    shutil.move(source_path, destination_path)
    print(f"Moved {file} to {destination_folder}")


if __name__ == "__main__":
    folder_path = r'C:\Users\dovgo\PycharmProjects\WEB-hw3\Temp'
    process_folder(folder_path)
