import sqlite3


def initiate_db():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
        )
        ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
        )
        ''')


    #cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', ('GPL® Man', 'Комплекс пептидов GPL Man для мужчин', 15900))
    #cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', ('Revilab ML 08', 'Для женского организма 2+1', 6600))
    #cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', ('От A до Zn', 'Витаминно-минеральный комплекс от А до Цинка для детей 3-7 лет груша', 209))
    #cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', ('Фемибион', 'Витаминно-минеральный комплекс для беременных', 2809))


    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('SELECT id, title, description, price FROM Products')
    users = cursor.fetchall()

    connection.commit()
    connection.close()
    return users


def add_user(username, email, age):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    existing_user = cursor.fetchone()

    if existing_user is None:
        cursor.execute('''
            INSERT INTO Users (username, email, age, balance) 
            VALUES (?, ?, ?, ?)''', (username, email, age, 1000))
        conn.commit()
    else:
        print(f"Пользователь с именем '{username}' уже существует.")


def is_included(username):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    return user is not None


initiate_db()
get_all_products()













