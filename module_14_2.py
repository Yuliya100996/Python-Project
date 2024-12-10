import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_username ON Users (username)')

#for i in range(10):
    #cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (f'User{1+i}', f'example{1+i}@gmail.com', f'{(i+1)*10}', 1000))

#cursor.execute("UPDATE Users SET balance = ? WHERE id%2 != ?", (500, 0))

#cursor.execute("DELETE FROM Users WHERE (id+2)%3 = ?", (0,))

#cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
#users = cursor.fetchall()
#for user in users:
    #print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс {user[3]}")

#cursor.execute("DELETE FROM Users WHERE id = ?", (6,))

cursor.execute("SELECT COUNT(*) FROM Users")
total_us = cursor.fetchone()[0]
print(total_us)

cursor.execute("SELECT SUM(balance) FROM Users")
total_bal = cursor.fetchone()[0]
print(total_bal)

cursor.execute("SELECT AVG(balance) FROM Users")
avg_bal = cursor.fetchone()[0]
print(avg_bal)

connection.commit()
connection.close()