import math
from src.Figure import Figure


class Circle(Figure):
    name = 'circle'

    def __init__(self, radius: int):
        self.radius = radius

    def area(self) -> float:
        area_value = round(math.pi * math.pow(self.radius, 2), 2)
        setattr(Circle, 'area_value', area_value)
        return area_value

    def perimeter(self) -> float:
        return round(2 * math.pi * self.radius, 2)
