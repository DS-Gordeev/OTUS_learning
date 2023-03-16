from src.Figure import Figure
from src.Rectangle import Rectangle


class Square(Figure, Rectangle):
    name = 'square'
    def __init__(self, side_a: int, side_b: int):
        super().__init__(side_a, side_b)
        # Невозможно создать квадрат с разными сторонами
        if self.side_a != self.side_b:
            raise ValueError
