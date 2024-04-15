import math
from typing import Tuple, Union

unit_lb = 2.20462
unit_oz = 16


def kgToLb(kg: float):
    """
    kg to lb oz
    1 千克 = 2.20462 磅
    1 磅 = 16 盎司
    """
    lb = kg * unit_lb
    oz = round((lb - int(lb)) * unit_oz, 3)

    return {'lb': lb, 'oz': oz}


print(kgToLb(float(input("输入KG:"))))


def is_leap_year(year: int) -> bool:
    """
    判断是否为闰年的规则：
    如果年份能被4整除但不能被100整除，则是闰年；
    如果年份能被400整除，则也是闰年。
    """

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


print(is_leap_year(int(input('输入年份:'))))


def calculate_circle(radius: float) -> Tuple[Union[float, int], Union[float, int]]:
    """
    输入半径计算圆的周长和面积
    """
    perimeter = 2 * math.pi * radius
    area = math.pi * radius ** 2
    return perimeter, area


circumference, area = calculate_circle(float(input("请输入圆的半径：")))
print(f"圆的周长为：{circumference:.2f}")
print(f"圆的面积为：{area:.2f}")
