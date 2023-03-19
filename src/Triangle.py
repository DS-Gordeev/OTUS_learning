import math
from src.Figure import Figure


class Triangle(Figure):
    name = 'triangle'

    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c
        # Невозможно создать треугольник с отрицательными сторонами
        if self.a < 0 or self.b < 0 or self.c < 0:
            raise ValueError
        # Треугольник можно создать только если сумма длин двух любых его сторон строго больше длины третьей
        if not (a + b > c) or not (a + c > b) or not (b + c > a):
            raise ValueError

    def perimeter(self) -> int:
        return self.a + self.b + self.c

    def area(self) -> float:
        # Определяем половину периметра треугольника для расчета площади по формуле Герона
        p = self.perimeter() / 2
        return round(math.sqrt(p*(p - self.a)*(p - self.b)*(p - self.c)), 2)
