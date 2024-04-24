"""
6.7
编写一个名为 printTable()的函数，它接受字符串的列表的列表，将它显示在组
织良好的表格中，每列右对齐。假定所有内层列表都包含同样数目的字符串

apples   Alice dogs
oranges  Bob   cats
cherries Carol moose
banana   David goose
"""

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(tableData):
    colWidths = [0] * len(tableData[0])

    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            colWidths[i] = max(colWidths[i], len(tableData[i][j]))

    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            print(tableData[j][i].ljust(colWidths[j]), end=' ')
        print()


printTable(tableData)
