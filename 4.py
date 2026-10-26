import random
class Student:


    def __init__(self, name,):
        self.name = name
        self.gladness = 30
        self.energy = 50
        self.progress = 10
        self.alive = True
        self.money = 50

    def study(self):
        print("Я прийшов навчатися до ІТ Step")
        self.progress += 1
        self.gladness += random.randint(0, 6) - 3
        self.energy -= 3
        self.money -= 7

    def request(self):
        print("Я попросив у мами гроші")
        self.money += 5

    def work(self):
        print("Я прийшов на підробіток")
        self.progress += 1
        self.gladness += random.randint(0, 6) - 3
        self.energy -= 4
        self.money += 15

    def chill(self):
        print("Я пішов гуляти з друзями")
        self.progress -= 1
        self.gladness += random.randint(2, 5)
        self.energy -= random.randint(1, 3)
        self.money -= random.randint(1, 3)

    def sleep(self):
        print("Я пішов спати")
        self.progress += 0
        self.gladness += random.randint(1, 3)
        self.energy += 7

    def eat(self):
        print("Я пішов їсти")
        self.progress += 0
        self.gladness += random.randint(1, 3)
        self.energy += 4
        self.money -= 2

    def info(self):
        print(f"Навченість : {self.progress}")
        print(f"Задоволення : {self.gladness}")
        print(f"Енергія : {self.energy}")
        print(f"Гроші : {self.money}")

    def is_alive(self):
        if self.progress <=0:
            print("У мене пусто в голові")
            self.alive = False
        if self.energy <=0:
            print("Я зовсім без сил")
            self.alive = False
        if self.gladness <=0:
            print("В мене діпресія")
            self.alive = False
        if self.progress > 100:
            print("Ура я стал академіком")
            self.alive = False
        if self.money <=0:
            print("Я залишився без грошей")
            self.alive = False



    def live(self, day):
        print(f"День №{day} з життя {self.name}")
        print("-"*30)

#==============================================
       # self.eat()
       # self.study()
     #   self.chill()
    #    self.work()
      #  self.sleep()

#==============================================


# ==============================================

        func = [self.study, self.chill, self.sleep, self.eat, self.work]
        random.choice(func)()



# ==============================================
        self.info()
        self.is_alive()
        print()

student = Student("Vasya")
for day in range(1, 366):
   if student.alive:
       student.live(day)

#day = 1
#while student.alive:
 #    student.live(day)
 #    day += 1
