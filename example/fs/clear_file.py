"""
9.8.2 删除不需要的文件
"""
import os


for foldername, subfolders, filenames in os.walk("../test"):
    for filename in filenames:
        size = os.path.getsize(os.path.join(os.path.abspath(foldername), filename))
        if size > 1024 * 4:
            print(os.path.join(os.path.abspath(foldername), filename))
            os.remove(os.path.join(os.path.abspath(foldername), filename))
