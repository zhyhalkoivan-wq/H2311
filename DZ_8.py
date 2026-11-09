class Animal:
    def __init__(self):
        self.breathe = "Дихає"
        self.move = "Рухається"

    def info(self):
        print(self.breathe)
        print(self.move)


class Mammals(Animal):
    def __init__(self):
        super().__init__()
        self.warm_blooded = "Теплокровна тварина"
        self.feed_milk = "Вигодовує молоком"

    def info(self):
        super().info()
        print(self.warm_blooded)
        print(self.feed_milk)


class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.fins = "Має плавці"
        self.gills = "Має зябра"

    def info(self):
        super().info()
        print(self.fins)
        print(self.gills)


class Cat(Mammals):
    def __init__(self):
        super().__init__()
        self.meow = "Нявкає"

    def info(self):
        super().info()
        print(self.meow)


class Dog(Mammals):
    def __init__(self):
        super().__init__()
        self.bark = "Гавкає"

    def info(self):
        super().info()
        print(self.bark)


class Goldfish(Fish):
    def __init__(self):
        super().__init__()
        self.gold_color = "Має золотистий колір"

    def info(self):
        super().info()
        print(self.gold_color)


a = Animal()
print("Animal:")
a.info()

m = Mammals()
print("\nMammals:")
m.info()

f = Fish()
print("\nFish:")
f.info()

c = Cat()
print("\nCat:")
c.info()

d = Dog()
print("\nDog:")
d.info()

g = Goldfish()
print("\nGoldfish:")
g.info()