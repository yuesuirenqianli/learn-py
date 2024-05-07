import zipfile


with zipfile.ZipFile('./01-03-2014eggs.zip', 'w') as zip:
    zip.write('./spam4-4-1984.txt', compress_type=zipfile.ZIP_DEFLATED)
