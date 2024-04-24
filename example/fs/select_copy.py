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
    with zipfile.ZipFile(zip_filename, 'a') as select_zip:
        for file_name in filter_files(folder_path):
            select_zip.write(os.path.join(folder_path, file_name), compress_type=zipfile.ZIP_STORED)


root_path = '../test/'
zip_path = '../test/select_zip.zip'


# TODO error zip content empty
add_to_zip(root_path, zip_path)
