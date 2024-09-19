class Vehicle:
    _COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, power):
        self.owner = owner
        self.__model = model
        self.__color = color
        self.__engine_power = power

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self._COLOR_VARIANTS:
            self.__color = new_color
            print(f'Вы сменили цвет на {new_color}')
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    _COLOR_VARIANTS = ['голубая лагуна', 'мокрый асфальт', 'чернозём', 'космос']
    __PASSENGERS_LIMIT = 5

    def print_info(self):
        print('='*20)
        super().print_info()
        print(f'Вместительность: {self.__PASSENGERS_LIMIT}')
        print('='*20)


if __name__ == '__main__':
    # Текущие цвета _COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

    # Изначальные свойства
    vehicle1.print_info()

    # Меняем свойства (в т.ч. вызывая методы)
    vehicle1.set_color('Pink')
    vehicle1.set_color('BLACK')
    vehicle1.set_color('КОСМОС')
    vehicle1.owner = 'Vasyok'

    # Проверяем что поменялось
    vehicle1.print_info()

