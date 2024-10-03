from math import pi as pi


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        if not self.__is_valid_color(*color):
            color = [0, 0, 0]
        self.__color = color

        if not self.__is_valid_side(*sides):
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)

        self.filled = False

    def get_color(self):
        return self.__color

    def get_sides(self):
        return self.__sides

    def __is_valid_side(self, *sides):
        return (
            all(isinstance(x, int) and x > 0 for x in sides)
            and len(sides) == self.sides_count
        )

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_color(self, r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_side(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * pi)

        def get_square(self):
            return pi * (self.__radius**2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        p = 0.5 * sum(self.get_sides)
        return (
            p * (p - self.get_sides[0])(p - self.get_sides[1])(p - self.get_sides[2])
        ) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) != 1:
            sides = [1]
        super().__init__(color, *sides * 12)

    def get_volume(self):
        return self.get_sides()[0] ** 3

    def set_sides(self, *sides):
        if len(sides) == 1:
            super().set_sides(*sides * 12)


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
