import pytest
from src.Circle import Circle
from src.Rectangle import Rectangle


@pytest.fixture(params=[10, 12, 15])
def create_circle(request):
    """Фикстура возвращает объект-окружность с разными радиусами"""
    return Circle(request.param)

@pytest.fixture(params=[(5, 8)])
def create_rectangle(request):
    """Фикстура возвращает объект-прямоугольник с указанными сторонами"""
    return Rectangle(*request.param)


class TestFigure:

    def test_add_area(self, create_rectangle, create_circle):
        create_circle.area()
        create_rectangle.area()
        assert getattr(create_circle, 'area_value') + getattr( create_rectangle, 'area_value')  == \
               create_rectangle.add_area(create_circle)


