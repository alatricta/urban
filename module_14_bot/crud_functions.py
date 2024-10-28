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


def get_all_products():
    with sq.connect(_NAME_DB) as connection:
        cursor = connection.cursor()
        cursor.execute('''
        SELECT * FROM Products
        ''')

        result = cursor.fetchall()
    return result


def add_product(title: str, description: str, price: float, img: str | None = None):
    with sq.connect(_NAME_DB) as connection:
        img = '' if (img is None) else img
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO Products (title, description, price, img)'
            f'VALUES ({title}, {description}, {price}, {img})'
        )


def del_product_by_id(id: int):
    with sq.connect(_NAME_DB) as connection:
        cursor = connection.cursor()
        cursor.execute(f'DELETE FROM Products WHERE id = {id}')


def __filling_db_from_file():
    from module_14_products_list import PRODUCTS

    with sq.connect(_NAME_DB) as connection:
        cursor = connection.cursor()

        for product in PRODUCTS:
            cursor.execute(
                'INSERT INTO Products (title, description, price, img)'
                f'VALUES ("{product["name"]}", "{product["description"]}", {product["price"]}, "{product["img"]}")'
            )


if __name__ == "__main__":
    # initiate_db()
    # __filling_db_from_file()
    print(get_all_products())
