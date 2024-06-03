import os

for foldername, subfolders, filenames in os.walk('./numbers'):
    for filename in filenames:
        os.remove(os.path.join(foldername, filename))
