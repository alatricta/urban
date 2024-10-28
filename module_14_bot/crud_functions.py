import sqlite3 as sq


_NAME_DB = 'module_14_bot/products.db'


def initiate_db():
    with sq.connect(_NAME_DB) as connection:
        cursor = connection.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL,
            img TEXT
            )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL
            )
        ''')


def add_user(username: str, email: str, age: int):
    with sq.connect(_NAME_DB) as connection:
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO Users (username, email, age, balance)'
            f' VALUES ("{username}", "{email}", {age}, 1000)'
            )


def is_included(username: str):
    users = tuple(u[1].casefold() for u in get_all_users())

    return username.casefold() in users


def get_all_products():
    with sq.connect(_NAME_DB) as connection:
        cursor = connection.cursor()
        cursor.execute(
            'SELECT * FROM Products'
        )

        result = cursor.fetchall()
    return result


def get_all_users():
    with sq.connect(_NAME_DB) as connection:
        cursor = connection.cursor()
        cursor.execute(
            'SELECT * FROM Users'
        )

        result = cursor.fetchall()
    return result


def add_product(title: str, description: str, price: float, img: str | None = None):
    with sq.connect(_NAME_DB) as connection:
        img = '' if (img is None) else img
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO Products (title, description, price, img)'
            f' VALUES ("{title}", "{description}", {price}, "{img}")'
        )


def del_product_by_id(id: int):
    with sq.connect(_NAME_DB) as connection:
        cursor = connection.cursor()
        cursor.execute(
            f'DELETE FROM Products WHERE id = {id}'
        )


def __filling_db_from_file():
    from module_14_products_list import PRODUCTS

    for product in PRODUCTS:
        add_product(product["name"], product["description"], product["price"], product["img"])


def __filing_users():
    with sq.connect(_NAME_DB) as connection:
        cursor = connection.cursor()

        count = 10
        for i in range(1, count+1):
            cursor.execute(
                'INSERT INTO Users (username, email, age, balance)'
                f' VALUES ("User{i}", "user{i}@example.ru", {i*10}, 1000)'
            )


if __name__ == "__main__":
    # initiate_db()
    # __filling_db_from_file()
    # __filing_users()
    print(get_all_products())
    print(get_all_users())
    # print(is_included('User1'))
