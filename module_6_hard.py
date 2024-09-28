import math


class Figure:
    sides_count = 0

    def __init__(self, color: list[int] | tuple[int], *sides: int):
        # if len(sides) != self.sides_count:
        #     self.__sides = tuple(1 for _ in range(self.sides_count))
        # else:
        #     self.__sides = sides
        self.__color = [*color] if self.__is_valid_color(*color) else [0, 0, 0]
        self.__sides = [*sides] if len(sides) == self.sides_count else [1] * self.sides_count
        self.filled = False

    def __len__(self):
        return sum(self.__sides)

    def get_color(self) -> tuple:
        return self.__color

    def __is_valid_color(self, r: int, g: int, b: int) -> bool:
        for num in (r, g, b):
            if (not isinstance(num, int)) or (num < 0) or (num > 255):
                return False
        return True

    def set_color(self, r: int, g: int, b: int) -> bool:
        if not self.__is_valid_color(r, g, b):
            # raise ValueError('Номера цветов должны быть в пределах от 0 до 255 включительно')
            return False
        self.__color = [r, g, b]
        return True

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *sides) -> bool:
        if len(sides) != self.sides_count:
            return False

        for num in sides:
            if (not isinstance(num, int)) or (num < 0):
                return False
        return True

    def set_sides(self, *new_sides) -> bool:
        if not self.__is_valid_sides(*new_sides):
            return False
        self.__sides = [*new_sides]
        return True


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: tuple[int, int, int], *sides: int):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    # def __init__(self, color: tuple[int, int, int], *sides: int):
    #     super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self.get_sides()
        p = (a + b + c) / 2
        res = math.sqrt(p * (p - a) * (p-b) * (p - c))
        return res


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: tuple[int, int, int], *sides: int):
        if len(sides) > 1:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides[0] for _ in range(self.sides_count))
        super().__init__(color, *self.__sides)

    def get_volume(self):
        return self.__sides[0] ** 3


def main():
    circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

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


if __name__ == '__main__':
    main()
