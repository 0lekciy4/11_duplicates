import os
import sys
from typing import Dict


def get_files_tree(path: str) -> Dict:
    file_tree = {}
    for root, _, file_names in os.walk(path):
        for file_name in file_names:
            file_info = (file_name, get_size_file(file_name, root))
            if file_info not in file_tree:
                file_tree[file_info] = []
            file_tree[file_info].append(root)
    return file_tree


def get_size_file(file_name: str, root_dir: str) -> int:
    file_path = path_join(file_name, root_dir)
    return os.path.getsize(file_path)


def path_join(file_name: str, root_dir: str) -> str:
    return os.path.join(root_dir, file_name)


def get_duplicates(file_tree: Dict) -> Dict:
    duplicates = {}
    for key, value in file_tree.items():
        if len(value) > 1:
            duplicates[key[0]] = [path_join(key[0], x) for x in value]
    return duplicates


def print_duplicated_files(duplicates: Dict):
    for file_name, paths in duplicates.items():
        print('File {} has duplicates:\n    {}'.format(file_name,
                                                       '\n    '.join(paths)))


def get_path_from_args() -> str:
    if os.path.exists(sys.argv[1]):
        return sys.argv[1]


def main():
    path = get_path_from_args()
    if path is None:
        print('Path is invalid')
        exit()
    file_dict = get_files_tree(path)
    duplicates = get_duplicates(file_dict)
    print_duplicated_files(duplicates)


if __name__ == '__main__':
    main()
