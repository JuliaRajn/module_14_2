import sqlite3

# Создать/подключиться к БД
conn = sqlite3.connect("not_telegram.db")
cursor = conn.cursor()


# Удалить запись с id = 6
cursor.execute("DELETE FROM Users WHERE id==6")

# Подсчитать общее количество записей
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

cursor.execute("DELETE FROM Users WHERE id=6")

# Подсчитать сумму всех балансов
cursor.execute("SELECT SUM(balance)  FROM Users")
all_balances = cursor.fetchone()[0]

# Вывести в консоль средний баланс всех пользователей
print(all_balances / total_users)
conn.commit()
conn.close()
