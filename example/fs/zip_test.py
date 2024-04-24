import zipfile


test_zip = zipfile.ZipFile('../test/test.zip', 'w')
test_zip.write('../test/', compress_type=zipfile.ZIP_DEFLATED)
test_zip.close()

