import math
from src.Figure import Figure


class Circle(Figure):
    name = 'circle'

    def __init__(self, radius: int):
        self.radius = radius
        # Невозможно создать окружность с отрицательным радиусом
        if self.radius < 0:
            raise ValueError

    def area(self) -> float:
        return round(math.pi * math.pow(self.radius, 2), 2)

    def perimeter(self) -> float:
        return round(2 * math.pi * self.radius, 2)
