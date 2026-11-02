import random


class House:
    def __init__(self):
        self.food = 0
        self.pollution = 0

    def __str__(self) -> str:
        return f"Будинок — їжа: {self.food}, забрудненість: {self.pollution}"


class Job:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Робота: {self.name}, зарплата: {self.salary}$"


class Car:
    def __init__(self, model):
        self.model = model
        self.fuel = 60
        self.state = 100

    def add_fuel(self):
        self.fuel += 20
        print("  • Автомобіль заправлено")

    def drive(self, length):
        rashod = length * 0.1
        if self.fuel - rashod > 0:
            print(f"  • Я проїхав {length} км, витратив {rashod} л пального")
            self.fuel -= rashod
            self.state -= length * 0.01
            return True
        else:
            print("  • Подорож не можлива, немає пального")
            return False

    def __str__(self) -> str:
        return f"Автомобіль: {self.model}, пальне: {round(self.fuel, 1)}л, стан: {round(self.state, 1)}%"


class Human:
    def __init__(self, name, car=None, job=None):
        self.name = name
        self.cars = [car] if car else []
        self.job = job
        self.house = House()
        self.money = 1000
        self.alive = True

    @property
    def current_car(self):
        return self.cars[-1] if self.cars else None

    def buy_car(self):
        if self.money - 3000 >= 200 and len(self.cars) < 2:
            self.money -= 3000
            new_car = Car("BMW")
            self.cars.append(new_car)
            print(f"  • Вітаємо! {self.name} купив 2-гу машину BMW за 3000$ (залишилось {self.money}$)! ")

    def work(self):
        if self.current_car is not None:
            print("  • Я поїхав на роботу")
        else:
            print("  • Я пішов на роботу")

        if self.job is not None:
            print(f"  • Я працюю: {self.job.name}, заробив сьогодні: {self.job.salary}$")
            self.money += self.job.salary
            self.buy_car()

    def shopping(self):
        print("  • Шопінг")
        money = random.randint(20, 30)
        food = random.randint(5, 10)
        if self.current_car is None:
            print("  • Я пішов в магазин пішки")
        else:
            if not self.current_car.drive(random.randint(10, 20)):
                print("  • Я пішов в магазин пішки")
        print(f"  • Я витратив {money}$ та придбав {food} продуктів")
        self.money -= money
        self.house.food += food

    def eat(self):
        eat_count = random.randint(2, 5)
        if self.house.food - eat_count > 0:
            print(f"  • Я смачно поїв {eat_count} продуктів")
            self.house.food -= eat_count
            self.house.pollution += random.randint(1, 5)
        else:
            print(f"  • Я хотів з'їсти {eat_count} продуктів, але їх немає")
            self.shopping()

    def chill(self):
        money = random.randint(10, 20)
        if self.money >= money:
            print(f"  • Я гарно відпочив і витратив {money}$")
            self.money -= money
            self.house.pollution += random.randint(1, 5)
        else:
            print("  • Я відпочиваю вдома, немає грошей")

    def cleaning(self):
        rnd = random.randint(1, 2)
        if rnd == 1:
            print("  • Я погонял пилюку")
            self.house.pollution -= 5
        else:
            print("  • Я зробив генеральне прибирання")
            self.house.pollution -= 15
        if self.house.pollution < 0:
            self.house.pollution = 0

    def info(self):
        print("\n--- ПАРАМЕТРИ ---")
        print(f"Гроші: {self.money}$")
        print(f"Кількість їжі у будинку: {self.house.food}")
        print(f"Забрудненість у домі: {self.house.pollution}")
        if self.cars:
            print("Машини в гаражі:")
            for index, c in enumerate(self.cars, 1):
                print(f"  - {index}-га машина: {c.model}")
        else:
            print("Машини: немає")

    def check_alive(self):
        if self.money < 0:
            print(f"\n--- {self.name} збанкрутував! ---")
            self.alive = False
        elif self.house.pollution > 100:
            print(f"\n--- У будинку {self.name} занадто брудно! ---")
            self.alive = False

    def live(self, day):
        print(f"\n==================== День №{day} з життя {self.name} ====================")
        print("--- ДІЇ ЗА ДЕНЬ ---")
        self.work()
        self.shopping()
        self.eat()
        self.chill()
        self.cleaning()

        self.info()
        self.check_alive()


human = Human("Vasya", job=Job("Programmer", 100), car=Car("Toyota"))

for day in range(1, 366):
    if human.alive:
        human.live(day)
    else:
        break