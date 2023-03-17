import math
from src.Figure import Figure


class Circle(Figure):
    name = 'circle'
    MIN_RADIUS = 0

    @classmethod
    def validate_radius(cls, arg):
        return arg >= cls.MIN_RADIUS

    # Невозможно создать окружность с отрицательным радиусом
    def __init__(self, radius: int):
        if self.validate_radius(radius):
            self.radius = radius
        else:
            raise ValueError

    def area(self) -> float:
        return round(math.pi * math.pow(self.radius, 2), 2)

    def perimeter(self) -> float:
        return round(2 * math.pi * self.radius, 2)
