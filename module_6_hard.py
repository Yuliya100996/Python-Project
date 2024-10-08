import math

class Figure:
    sides_count = 0

    def __init__(self, color: list, *sides: int):
        self.__color = [*color] if self.__is_valid_color(*color) else [0, 0, 0]
        self.__sides = [*sides] if len(sides) == self.sides_count else [1] * self.sides_count
        self.filled = False

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_color(self, r, g, b):
        return all(isinstance(c, int) and 0 <= c <= 255 for c in [r, g, b])

    def __is_valid_sides(self, sides):
        return all(isinstance(side, int) and side > 0 for side in sides) and len(sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.get_sides())

    def set_sides(self, *sides):
        if self.__is_valid_sides(sides):
            self.__sides = list(sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color: str, *sides: int):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        p = len(self) / 2
        a, b, c = self.get_sides()
        return math.sqrt(p * (p-a) * (p-b) * (p-c))

class Cude(Figure):
    sides_count = 12

    def __init__(self, color: list, *sides: int):
        super().__init__(color, *sides)
        self.set_sides(*list(sides) * 12)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cude((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())









