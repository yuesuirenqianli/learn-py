"""
    10.1
    当 Python 试图执行无效代码时，就会抛出异常。在第 3 章中，你已看到如何使
    用 try 和 except 语句来处理 Python 的异常，这样程序就可以从你预期的异常中恢复。
    但你也可以在代码中抛出自己的异常。抛出异常相当于是说：“停止运行这个函数
    中的代码，将程序执行转到 except 语句 ”。
    抛出异常使用 raise 语句。在代码中，raise 语句包含以下部分：
        raise 关键字；
        对 Exception 函数的调用；
        传递给 Exception 函数的字符串，包含有用的出错信息。
"""


from abc import ABC, abstractmethod


class PrintStrategy(ABC):
    @abstractmethod
    def print(self, symbol, width, height):
        pass


class SimplePrintStrategy(PrintStrategy):
    def print(self, symbol, width, height):
        if len(symbol) != 1:
            raise Exception('Symbol must be a single character string.')
        if width <= 2:
            raise Exception('Width must be greater than 2.')
        if height <= 2:
            raise Exception('Height must be greater than 2.')

        print(symbol * width)
        for i in range(height - 2):
            print(symbol + (' ' * (width - 2)) + symbol)
            print(symbol * width)


class Printer:
    def __init__(self, strategy: PrintStrategy):
        self.strategy = strategy

    def print(self, symbol, width, height):
        self.strategy.print(symbol, width, height)


class PrinterFactory:
    @staticmethod
    def create_printer(strategy: PrintStrategy):
        return Printer(strategy)


def main():
    strategies = {
        'simple': SimplePrintStrategy()
    }

    for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
        try:
            printerIns = PrinterFactory.create_printer(strategies['simple'])
            printerIns.print(sym, w, h)
        except Exception as err:
            print('An exception happened: ' + str(err))


if __name__ == '__main__':
    main()
