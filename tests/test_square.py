import pytest
from src.Square import Square

class TestSquare:

    @pytest.mark.parametrize("side, area", [(1, 1), (0, 0), (15, 225)])
    def test_square_area(self, side, area):
        square = Square(side)
        assert square.area() == area, f'Ошибка в подсчете площади Квадрата со сторонами - {side}'

    @pytest.mark.parametrize("side, perimetr", [(1, 4), (0, 0), (8, 32)])
    def test_square_perimeter(self, side, perimetr):
        square = Square(side)
        assert square.perimeter() == perimetr, f'Ошибка в подсчете периметра Квадрата со сторонами - {side}'

    @pytest.mark.parametrize("attr_name", ['name', 'area', 'perimeter'])
    def test_square_hasattr(self, attr_name):
        square = Square(1)
        assert hasattr(square, attr_name), f'У объекта отсутствует обязательный атрибут - {attr_name}'
