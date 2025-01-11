import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS USERS(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER, 
balance INTEGER NOT NULL
)
''')

cursor.execute('''
DELETE FROM Users
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                (f"User{i}", f"example{i}@gmail.com", 10*i, "1000"))

for i in range(1,11):
    if i % 2 == 1:
        cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, i))

for i in range(1,11):
    if i % 3 == 1:
        cursor.execute("DELETE FROM Users WHERE id = ?", (i,))

cursor.execute("SELECT username, age FROM Users WHERE age != 60")
users = cursor.fetchall()
for user in users:
    print(user)

connection.commit()
connection.close()
