from src.Figure import Figure


class Rectangle(Figure):
    name = 'rectangle'

    def __init__(self, side_a: int, side_b: int):
        self.side_a = side_a
        self.side_b = side_b
        # Невозможно создать фигуру с отрицательными сторонами
        if self.side_a < 0 or self.side_b < 0:
            raise ValueError

    def area(self) -> int:
        return self.side_a * self.side_b

    def perimeter(self) -> int:
        return (self.side_a + self.side_b) * 2
