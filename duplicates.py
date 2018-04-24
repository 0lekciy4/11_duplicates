import os
import sys
from typing import Dict


def get_files_tree(path: str) -> Dict:
    """
    Get all files and absolute paths to it.

    :param path: path to check for duplicate files
    :type path: str
    :return: dict with tuple as (key) where first value in tuple - filename,
                                          second value in tuple - filesize,
                                [value] list with abs paths to files
    :rtype: dict(tuple:list)
    """
    file_tree = {}
    for root, subdirs, file_names in os.walk(path):
        for file_name in file_names:
            file_info = (file_name, get_size_file(file_name, root))
            if not file_info in file_tree:
                file_tree[file_info] = []
            file_tree[file_info].append(root)
    return file_tree


def get_size_file(file_name: str, root_dir: str) -> int:
    """
       Get size of file.

       :param file_name: name of file
       :type file_name: str
       :param root_dir: absolute path to folder with this file
       :type root_dir: str

       :return: size of file
       :rtype: int
    """
    file_path = path_join(file_name, root_dir)
    return os.path.getsize(file_path)


def path_join(file_name: str, root_dir: str) -> str:
    """
       Make absolute path to file.

       :param file_name: name of file
       :type file_name: str
       :param root_dir: absolute path to folder with this file
       :type root_dir: str

       :return: absolute path to this file
       :rtype: str
    """
    return os.path.join(root_dir, file_name)


def get_duplicates(file_tree: Dict) -> Dict:
    """
    Get list of lists with duplicate files.

    :param file_tree: dict with tuple as (key) where first value in tuple - filename,
                                                     second value in tuple - filesize,
                                         [value] list with abs paths to files
    :return: dict with filename as 'key'
            and duplicates list as [value]
    """
    duplicates = {}
    for key, value in file_tree.items():
        if len(value) > 1:
            duplicates[key[0]] = [path_join(key[0], x) for x in value]
    return duplicates


def print_duplicated_files(duplicates: Dict):
    """
    Prints files and duplicated paths
    :param duplicates: dict with filename as 'key'
            and duplicates list as [value]
    """
    for file_name, paths in duplicates.items():
        print('File {} has duplicates:\n    {}'.format(file_name,
                                                       '\n    '.join(paths)))


def get_path_from_args() -> str:
    """
    Gets path to check it.

    :rtype: str
    :return: folder path
    """
    if not os.path.exists(sys.argv[1]):
        print('Path is invalid')
        sys.exit()
    return sys.argv[1]


def main():
    """
    Main function, implements main logic.

    :return: print result of our script.
    """
    path = get_path_from_args()
    file_dict = get_files_tree(path)
    duplicates = get_duplicates(file_dict)
    print_duplicated_files(duplicates)


if __name__ == '__main__':
    main()
