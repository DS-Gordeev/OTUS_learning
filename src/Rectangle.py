from src.Figure import Figure


class Rectangle(Figure):
    name = 'rectangle'

    def __init__(self, rec_side_a: int, rec_side_b: int):
        self.rec_side_a = rec_side_a
        self.rec_side_b = rec_side_b

    def area(self) -> int:
        area_value = self.rec_side_a * self.rec_side_b
        setattr(Rectangle, 'area_value', area_value)
        return area_value

    def perimeter(self) -> int:
        return self.rec_side_a * 2 + self.rec_side_b * 2
