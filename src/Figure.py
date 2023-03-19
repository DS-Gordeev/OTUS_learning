class Figure:
    def add_area(self, obj):
        # Проверяем, что переданный объект является подклассам базового класса, т.е. фигурой
        if issubclass(type(obj), Figure):
            return self.area() + obj.area()
        else:
            raise ValueError
