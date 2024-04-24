import shutil
import os
import re
import zipfile


def copy_file(src, dest):
    return shutil.copy(src, dest)


def copy_dir(src, dest):
    return shutil.copytree(src, dest)


def move(src, target):
    return shutil.move(src, target)


def remove_dis(path):
    has_remove = input(f'是否删除{path}下所有文件?(yes or no) ')

    if not re.search('yes|y', has_remove):
        print('取消')
        return

    shutil.rmtree(path)


def create_dis(path):
    os.makedirs(path, exist_ok=True)


def file_list():
    for cur_file, child_file, filenames in os.walk('./test'):
        print(str('').rjust(10, '-'), cur_file)

        for filename in filenames:
            print(str('').rjust(15, '-'), filename)

        for child in child_file:
            print(str('').rjust(15, '-'), child)


def create_zip():
    new_zip = zipfile.ZipFile('test.zip', 'w')
    new_zip.write('./test/bullet_point_adder.py', compress_type=zipfile.ZIP_DEFLATED)
    new_zip.close()


def append_zip():
    cur_zip = zipfile.ZipFile('test.zip', 'a')
    cur_zip.write('./calc_copy.py', compress_type=zipfile.ZIP_DEFLATED)
    cur_zip.close()


def extractall():
    exampleZip = zipfile.ZipFile('./test.zip')
    exampleZip.extractall('./test1')
    exampleZip.close()


def compile_util():
    with open('./utils/file_util.py', 'r') as file_util:
        file_util = file_util.read()

    with open('./utils/path_util.py', 'r') as path_util:
        path_util = path_util.read()

    content = file_util + '\n' + path_util

    with open('./utils/index.py', 'w') as index_util:
        index_util.write(content)


compile_util()
