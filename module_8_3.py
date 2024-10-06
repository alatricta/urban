class IncorrectVinNumber(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message


class IncorrectCarModels(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message


class Car:
    def __init__(self, model: str, vin: int, number: str):
        self.model = model
        self.vin = vin
        self.number = number
        # self.__model = model if self.__is_valid_model(model) else None
        # self.__vin = vin if self.__is_valid_vin(vin) else None
        # self.__number = number if self.__is_valid_numbers(number) else None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if self.__is_valid_model(model):
            self.__model = model

    @property
    def vin(self):
        return self.__vin

    @vin.setter
    def vin(self, vin):
        if self.__is_valid_vin(vin):
            self.__vin = vin

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if self.__is_valid_numbers(number):
            self.__number = number

    def __is_valid_model(self, model):
        if not isinstance(model, str):
            raise IncorrectCarModels("Неверный тип данных модели машины")
        return True

    def __is_valid_vin(self, vin):
        if not isinstance(vin, int):
            raise IncorrectVinNumber("Некорректный тип vin номера")
        if vin < 1_000_000 or vin > 9_999_999:
            raise IncorrectVinNumber("Некорректный диапазон для vin номера")
        return True

    def __is_valid_numbers(self, number):
        if not isinstance(number, str):
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")
        if len(number) != 6:
            raise IncorrectCarNumbers("Неверная длина номера")
        return True


def main():
    try:
        first = Car("Model1", 1000000, "f123dj")
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f"{first.model} успешно создан")

    try:
        second = Car("Model2", 300, "т001тр")
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f"{second.model} успешно создан")

    try:
        third = Car("Model3", 2020202, "нет номера")
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f"{third.model} успешно создан")

    first.model = "Sarancha M-10"
    print(first.model)


if __name__ == "__main__":
    main()
