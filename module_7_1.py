from os.path import exists


class Product:
    def __init__(self, name: str, weight: float, category: str) -> None:
        self.name = name
        self.weight = weight
        self.category = category

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError('Неверный формат ввода: должна быть строка (str)')
        self.__name = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if isinstance(value, int | float):
            self.__weight = value
        else:
            try:
                self.__weight = float(value)
            except Exception as e:
                raise ValueError(f'Ошибка назначения параметра:\n{e}')

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError('Неверный формат ввода: должна быть строка (str)')
        self.__category = str(value)

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Product):
            return self.name == value.name and \
                self.weight == value.weight and \
                self.category == value.category
        elif isinstance(value, str):
            return self.name.lower() == value.lower()
        else:
            raise ValueError(
                f'Невозможно сравнить с объектом типа {type(value)}')

    def __contains__(self, value):
        if isinstance(value, Product):
            return self.name == value.name
        elif isinstance(value, str):
            return self.name.lower() == value.lower()
        else:
            raise ValueError(
                f'Невозможно сравнить с объектом типа {type(value)}')

    def __str__(self) -> str:
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self) -> None:
        self.__file_name = 'module_7_1_products.txt'
        if not exists(self.__file_name):
            open(self.__file_name, 'w').close()

    def get_products(self) -> str:
        # f = open(self.__file_name, 'r')
        # s = f.read()
        # f.close()
        with open(self.__file_name, 'r') as f:
            return f.read()

    def add(self, *products: Product) -> None:
        with open(self.__file_name, 'r') as f:
            has_products = f.read().splitlines()

        has_products = list(Product(*x.split(', ')) for x in has_products)

        for product in products:
            for i, has_product in enumerate(has_products):
                if product in has_product:
                    # print(f"Продукт {product.name} уже есть в магазине")

                    # Но можно немножко доработать
                    ch = input(f'Продукт {product.name} уже есть в магазине:\n'
                               '1 - Пропустить добавление этого продукт\n'
                               '2 - Заменить имеющийся продукт новым\n'
                               '3 - Суммировать массу продуктов\n'
                               '4 - Прекратить выполнение\n'
                               'Ваш выбор: ')
                    match ch:
                        case '1':
                            break
                        case '2':
                            has_products[i] = product
                            break
                        case '3':
                            has_product.weight += product.weight
                            break
                        case '4':
                            return False
            else:
                has_products.append(product)

        with open(self.__file_name, 'w') as f:
            for product in has_products:
                f.write(f'{product}\n')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

print(p1 == p3)
p4 = Product('Potato', 50.5, 'Vegetables')
print(p1 == p4)
print('Potato' == p1)
print('Spaghetti' in p2)
