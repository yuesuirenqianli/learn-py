import os
import re

numbers = []
for foldername, subfolders, filenames in os.walk("./numbers"):
    for filename in filenames:
        numbers.append(int(re.search('\d+', filename).group()))


def find_missing_elements(array):
    missing_elements = []
    for i in range(len(array) - 1):
        if array[i + 1] - array[i] != 1:
            missing_elements.extend(range(array[i] + 1, array[i + 1]))
    return missing_elements


missing_elements = find_missing_elements(numbers)

print("缺少的元素：", missing_elements)
