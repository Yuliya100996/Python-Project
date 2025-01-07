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


    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', ('GPL® Man', 'Комплекс пептидов GPL Man для мужчин', 15900))
    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', ('Revilab ML 08', 'Для женского организма 2+1', 6600))
    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', ('От A до Zn', 'Витаминно-минеральный комплекс от А до Цинка для детей 3-7 лет груша', 209))
    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', ('Фемибион', 'Витаминно-минеральный комплекс для беременных', 2809))

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


initiate_db()
get_all_products()












