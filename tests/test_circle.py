import pytest
from src.Circle import Circle


class TestCircle:

    @pytest.mark.parametrize("radius, area", [(1, 3.14), (0, 0), (14, 615.75)])
    def test_circle_area(self, radius, area):
        circle = Circle(int(radius))
        assert circle.area() == area, f'Ошибка в подсчете площади Круга радиусом - {radius}'

    @pytest.mark.parametrize("radius, length", [(1, 6.28), (0, 0), (23, 144.51)])
    def test_circle_length(self, radius, length):
        circle = Circle(int(radius))
        assert circle.perimeter() == length, f'Ошибка в подсчете длины окружности радиусом - {radius}'

    @pytest.mark.parametrize("attr_name", ['name', 'area', 'perimeter'])
    def test_circle_hasattr(self, attr_name):
        circle = Circle(1)
        assert hasattr(circle, attr_name), f'У объекта отсутствует обязательный атрибут - {attr_name}'
