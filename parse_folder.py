import sys
from colorama import Fore
from pathlib import Path

path = sys.argv[1]
parent_folder_path = Path(path)

if len(sys.argv) < 2:
    print("Usage: python hw03.py <directory>")

def parse_folder(path, indent=""):
    try:
        for element in path.iterdir():
            if element.is_dir():
                print(f'{indent}📂{Fore.BLUE}{element.name}')
                parse_folder(element, indent + "|")
            elif element.is_file() and '.py' in element.name:
                print(f'{indent}📜{Fore.MAGENTA}{element.name}')
            elif element.is_file():
                print(f'{indent}📜{Fore.GREEN}{element.name}')
    except Exception as e:
        print(f'{Fore.RED}{e}')
parse_folder(parent_folder_path)