"""
    10.1
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
