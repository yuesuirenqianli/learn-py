import math
from typing import Tuple, Union
from abc import ABC, abstractmethod


class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance.UNIT_LB = 2.20462
            cls._instance.UNIT_OZ = 16
        return cls._instance


class CalculationStrategy(ABC):
    @abstractmethod
    def calculate(self):
        pass


class WeightConverter(CalculationStrategy):
    def __init__(self, kg: float):
        self.kg = kg

    def calculate(self) -> dict:
        lb = self.kg * config.UNIT_LB
        oz = round((lb - int(lb))*config.UNIT_OZ, 3)
        return {'lb': lb, 'oz': oz}


class LeapYearChecker(CalculationStrategy):
    def __init__(self, year: int):
        self.year = year

    def calculate(self) -> bool:
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)


class Circle(CalculationStrategy):
    def __init__(self, radius: float):
        self.radius = radius

    def calculate(self) -> Tuple[Union[float, int], Union[float, int]]:
        perimeter = 2 * math.pi * self.radius
        area = math.pi * self.radius ** 2
        return perimeter, area


class CalculationFactory:
    @staticmethod
    def create_calculator(calculation_type: str, value: float) -> CalculationStrategy:
        if calculation_type == "weight":
            return WeightConverter(value)
        elif calculation_type == "leap_year":
            return LeapYearChecker(int(value))
        elif calculation_type == "circle":
            return Circle(value)
        else:
            raise ValueError(f"Unknown calculation type: {calculation_type}")


def main():
    kg = float(input("输入KG:"))
    weight_converter = CalculationFactory.create_calculator("weight", kg)
    result = weight_converter.calculate()
    print(f"{kg} kg 转换为 {result['lb']} 磅 {result['oz']} 盎司")

    year = int(input("输入年份:"))
    leap_year_checker = CalculationFactory.create_calculator("leap_year", year)
    if leap_year_checker.calculate():
        print(f"{year} 是闰年")
    else:
        print(f"{year} 不是闰年")

    radius = float(input("输入圆的半径:"))
    area = CalculationFactory.create_calculator("circle", radius)
    perimeter, area = area.calculate()
    print(f"圆的周长为: {perimeter:.2f}")
    print(f"圆的面积为: {area:.2f}")


if __name__ == "__main__":
    config = Config()
    main()
