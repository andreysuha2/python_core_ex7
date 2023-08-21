from .utils.normalize import normalize as normalize_name
from sys import argv
from pathlib import Path
from .config.config import OTHER_FOLDER as OTHER_FOLDER, FOLDERS_DATA as FOLDERS_DATA
import os

if len(argv) < 2:
    print('Param folder is required!')
    exit()

default_path = Path(argv[1])

def create_directories(path):
    for name in FOLDERS_DATA:
        folder_path = f"{path.parent}/{path.name}/{name}"

        if not Path(folder_path).exists():
            os.mkdir(folder_path)

def create_file_name(path, ext, counter = 0):
    file_name = f"{path}{ext}" if not counter else f"{path}_{counter}{ext}"
    return create_file_name(path, ext, counter + 1) if os.path.exists(file_name) else file_name           

def handle_file(path): 
    parent_folder_name = OTHER_FOLDER
    file = path.name.split('.')
    file_ext = file.pop()
    file_name = '.'.join(file)
    for name, list in FOLDERS_DATA.items():
        if file_ext.upper() in list:
            parent_folder_name = name
            break

    if parent_folder_name:
        file_name = create_file_name(f"{default_path}/{parent_folder_name}/{normalize_name(file_name)}", path.suffix)
        os.rename(path, file_name)
        print(path, '-->', file_name)

def arrange(path):
    if not path.exists():
        print(f"Folder '{path.name}' in '{path.parent}' doesn't exist!")
    elif path.is_file():
        print(f"'{path.name}' is not a folder!")
    else:
        for i in path.iterdir():
            if i.is_dir() and i.name not in FOLDERS_DATA:
                arrange(i)
                try:
                    os.rmdir(i)
                except OSError as error:
                    print(error)
                    print(f"Path {i} can't be removed")
            elif i.is_file():
                handle_file(i)

def main():
        if len(argv) < 2:
            print('Param folder is required!')
            exit()

        global default_path
        default_path = Path(argv[1])
        create_directories(default_path)
        arrange(default_path)

if __name__ == '__main__':
    main()