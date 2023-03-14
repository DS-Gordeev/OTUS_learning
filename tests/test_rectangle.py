import pytest
from src.Rectangle import Rectangle


class TestRectangle:

    @pytest.mark.parametrize("a, b, area", [(1, 1, 1), (0, 0, 0), (6, 32, 192)])
    def test_rectangle_area(self, a, b, area):
        rectangle = Rectangle(a, b)
        assert rectangle.area() == area, f'Ошибка в подсчете площади Прямоугольника со сторонами - {a , b}'

    @pytest.mark.parametrize("a, b, perimeter", [(1, 1, 4), (0, 0, 0), (10, 48, 116)])
    def test_rectangle_perimetr(self, a, b, perimeter):
        rectangle = Rectangle(a, b)
        assert rectangle.perimeter() == perimeter, f'Ошибка в подсчете периметра Прямоугольника со сторонами - {a, b}'

    @pytest.mark.parametrize("attr_name", ['name', 'area', 'perimeter'])
    def test_square_hasattr(self, attr_name):
        square = Rectangle(1, 1)
        assert hasattr(square, attr_name), f'У объекта отсутствует обязательный атрибут - {attr_name}'
