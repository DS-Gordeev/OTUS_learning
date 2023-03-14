class Figure:
    def add_area(self, obj):
        # Проверяем, что переданный объект является подклассам базового класса, т.е. фигурой
        if issubclass(type(obj), Figure):
            return getattr(self, 'area_value') + getattr(obj, 'area_value')
        else:
            raise ValueError
