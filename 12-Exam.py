import sqlite3

connection = sqlite3.connect("finance.sl3")
cur = connection.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS finance (id INTEGER, amount REAL, type TEXT, description TEXT)")
connection.commit()

while True:
    print("\n1 - Додати дохід")
    print("2 - Додати витрату")
    print("3 - Переглянути операції")
    print("4 - Переглянути баланс")
    print("0 - Вихід")

    choice = input("Вибір: ")

    if choice == "1" or choice == "2":
        amount = input("Сума: ")
        description = input("Опис: ")

        if choice == "1":
            type = "Дохід"
        else:
            type = "Витрата"

        cur.execute("INSERT INTO finance (amount, type, description) VALUES (" + amount + ", '" + type + "', '" + description + "')")
        connection.commit()

        print("Операцію додано!")

    elif choice == "3":
        cur.execute("SELECT * FROM finance")
        res = cur.fetchall()

        for row in res:
            print(row)

    elif choice == "4":
        cur.execute("SELECT SUM(amount) FROM finance WHERE type = 'Дохід'")
        income = cur.fetchall()[0][0]

        cur.execute("SELECT SUM(amount) FROM finance WHERE type = 'Витрата'")
        expenses = cur.fetchall()[0][0]

        if income == None:
            income = 0

        if expenses == None:
            expenses = 0

        print("Доходи:", income)
        print("Витрати:", expenses)
        print("Баланс:", income - expenses)

    elif choice == "0":
        break

    else:
        print("Невірний вибір!")

connection.close()
