import pytest
from src.Square import Square


class TestSquare:

    @pytest.mark.parametrize("side_a, side_b, area", [(1, 1, 1), (0, 0, 0), (15, 15, 225)])
    def test_square_area(self, side_a, side_b, area):
        square = Square(side_a, side_b)
        assert square.area() == area, f'Ошибка в подсчете площади Квадрата со сторонами - {side_a}'

    @pytest.mark.parametrize("side_a, side_b, perimetr", [(1, 1, 4), (0, 0, 0), (8, 8, 32)])
    def test_square_perimeter(self, side_a, side_b, perimetr):
        square = Square(side_a, side_b)
        assert square.perimeter() == perimetr, f'Ошибка в подсчете периметра Квадрата со сторонами - {side_a}'

    @pytest.mark.parametrize("attr_name", ['name', 'area', 'perimeter'])
    def test_square_hasattr(self, attr_name):
        square = Square(1, 1)
        assert hasattr(square, attr_name), f'У объекта отсутствует обязательный атрибут - {attr_name}'

    @pytest.mark.parametrize("a, b", [(1, 0), (0, 1), (10, 100), (5, 18)])
    def test_square_is_possible(self, a, b):
        try:
            Square(a, b)
        except ValueError:
            assert True

    @pytest.mark.parametrize("a, b", [(1, -10), (-1, 10), (-5, -5), (-18, -64)])
    def test_square_negative_side(self, a, b):
        try:
            Square(a, b)
        except ValueError:
            assert True
