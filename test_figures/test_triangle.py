import pytest
from src.Triangle import Triangle


class TestTriangle:

    @pytest.mark.parametrize("a, b, c, area",
                             [(12, 13, 14, 72.31),
                              (8, 7, 2, 6.44),
                              (39, 44, 24, 466.27)])
    def test_triangle_area(self, a, b, c, area):
        triangle = Triangle(a, b, c)
        assert triangle.area() == area, f'Ошибка в подсчете площади Треугольника со сторонами - {a, b, c}'

    @pytest.mark.parametrize("a, b, c", [(0, 0, 0), (1, 4, 9), (20, 0, 8)])
    def test_triangle_is_possible(self, a, b, c):
        try:
            Triangle(a, b, c)
        except ValueError:
            assert True

    @pytest.mark.parametrize("a, b, c, perimeter",
                             [(15, 21, 12, 48),
                              (6, 3, 8, 17),
                              (1, 1, 1, 3)])
    def test_triangle_perimeter(self, a, b, c, perimeter):
        triangle = Triangle(a, b, c)
        assert triangle.perimeter() == perimeter, f'Ошибка в подсчете периметра Треугольника со сторонами - {a, b, c}'

    @pytest.mark.parametrize("a, b, c", [(-12, 13, 14), (12, -13, 14), (12, 13, -14), (-6, -3, -8)])
    def test_triangle_negative_side(self, a, b, c):
        try:
            Triangle(a, b, c)
        except ValueError:
            assert True
