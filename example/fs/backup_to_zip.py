"""
9.5 假定你正在做一个项目，它的文件保存在 C:\\AlsPythonBook 文件夹中。你担心工作
会丢失，所以希望为整个文件夹创建一个 ZIP 文件，作为“快照”。你希望保存不同的版
本，希望 ZIP 文件的文件名每次创建时都有所变化。例如 AlsPythonBook_1.zip、
AlsPythonBook_2.zip、AlsPythonBook_3.zip，等等。你可以手工完成，但这有点烦人，
而且可能不小心弄错 ZIP 文件的编号。运行一个程序来完成这个烦人的任务会简单得多。
"""

import zipfile
import os


def backup_to_zip():
    folder = os.path.abspath('.')

    number = 1

    while True:
        zipFilename = os.path.basename(folder) + "_" + str(number) + ".zip"

        if not os.path.exists(zipFilename):
            break
        number += 1

    with zipfile.ZipFile(zipFilename, 'w') as zip:
        for foldername, subfolders, files in os.walk(folder):
            zip.write(foldername)
            for filename in files:
                newBase = os.path.basename(folder) + '_'
                if filename.startswith(newBase) and filename.endswith('.zip'):
                    continue

                zip.write(os.path.join(foldername, filename))


backup_to_zip()
