"""
6.4
在编辑一篇维基百科的文章时，你可以创建一个无序列表，即让每个列表项占
据一行，并在前面放置一个星号。但是假设你有一个非常大的列表，希望添加前面
的星号。你可以在每一行开始处输入这些星号，一行接一行。或者也可以用一小段
Python 脚本，将这个任务自动化。
"""

import pyperclip


class TextProcessor:
    def __init__(self, text=''):
        self.text = text

    def paste_text(self):
        self.text = pyperclip.paste()

    def add_line_numbers(self):
        lines = self.text.split('\n')
        for i in range(len(lines)):
            lines[i] = str(i + 1) + ' ' + lines[i]
        self.text = '\n'.join(lines)

    def copy_text(self):
        pyperclip.copy(self.text)

    def process_text(self):
        self.paste_text()
        self.add_line_numbers()
        self.copy_text()


def main():
    processor = TextProcessor()
    processor.process_text()


if __name__ == '__main__':
    main()
