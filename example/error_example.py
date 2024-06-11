"""
    10.2
    如果 Python 遇到错误，它就会生成一些错误信息，称为“反向跟踪”。反向跟踪
    包含了出错消息、导致该错误的代码行号，以及导致该错误的函数调用的序列。这
    个序列称为“调用栈”。
"""

import traceback


def spam():
    bacon()


def bacon():
    try:
        raise Exception('This is the error message.')
    except Exception as e:
        errorFile = open('error.txt', 'w')
        errorFile.write(traceback.format_exc())
        errorFile.close()
        print('The traceback info was written to errorInfo.txt.')
        print(e)


spam()
