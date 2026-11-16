import sqlite3
import hashlib

connection = sqlite3.connect("db.sl3", timeout=5)
cur = connection.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users (login TEXT, password TEXT, name TEXT)")
connection.commit()

choice = input("1 - Login\n2 - Registration\nВибір: ")

if choice == "1":
    login = input("Login : ")
    passw = input("Password : ")

    h = hashlib.sha256()
    h.update(passw.encode())
    h_passw = h.hexdigest()

    cur.execute(f"SELECT * FROM users WHERE login = '{login}' AND password = '{h_passw}'")
    res = cur.fetchall()

    if res:
        print("Ви успішно увійшли!")
        print("Вітаємо,", res[0][2])
    else:
        print("Неправильний логін або пароль!")

elif choice == "2":
    login = input("Login : ")
    passw = input("Password : ")
    name = input("NickName : ")

    h = hashlib.sha256()
    h.update(passw.encode())
    h_passw = h.hexdigest()

    cur.execute(f"SELECT * FROM users WHERE login = '{login}'")
    res = cur.fetchall()

    if res:
        print("Такий логін вже існує!")
    else:
        cur.execute(f"INSERT INTO users (login, password, name) VALUES('{login}', '{h_passw}', '{name}')")
        connection.commit()
        print("Вітаємо на сайті!")

else:
    print("Невірний вибір!")

connection.close()