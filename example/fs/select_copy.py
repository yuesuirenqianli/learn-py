"""
9.8.1
"""
import zipfile
import re
import os


def file_num(file_name):
    reg = re.compile(r'\d+')
    target = reg.search(file_name)
    if target:
        return int(target.group(0))
    return -1


def filter_files(folder_path):
    res = []
    for file_name in os.listdir(folder_path):
        file_idx = file_num(file_name)
        if file_idx != -1 and file_idx % 2 == 0:
            res.append(file_name)
    return res


def add_to_zip(folder_path, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w') as zip:
        for file_name in filter_files(folder_path):
            zip.write(os.path.join(os.path.abspath(folder_path), file_name))


root_path = '../test'
zip_path = './select_zip.zip'


add_to_zip(root_path, zip_path)
