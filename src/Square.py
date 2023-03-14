from src.Figure import Figure


class Square(Figure):
    name = 'square'

    def __init__(self, square_side: int):
        self.square_side = square_side

    def area(self) -> int:
        area_value = self.square_side * self.square_side
        setattr(Square, 'area_value', area_value)
        return self.square_side * self.square_side

    def perimeter(self) -> int:
        return self.square_side * 4
