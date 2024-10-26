import sqlite3 as sq


with sq.connect('not_telegram.db') as connection:
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL
        )
        ''')

    count = 10
    for i in range(1, count+1):
        cursor.execute('''
        INSERT INTO users (id, username, email, age, balance) VALUES (?,?,?,?,?)''',
                      (i, 
                       f'User{i}',
                       f'user{i}@example.ru',
                       f'{i*10}',
                       1000))

    for i in range(1, count+1, 2):
        cursor.execute('UPDATE users SET balance=? WHERE id=?', (500, i))

    for i in range(1, count+1, 3):
        cursor.execute('DELETE FROM users WHERE id = ?', (i, ))

    cursor.execute('SELECT username, email, age, balance FROM users WHERE age != 60')
    Users = cursor.fetchall()
    for user in Users:
        username = user[0]
        email = user[1]
        age = user[2]
        balance = user[3]
        print(f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')
