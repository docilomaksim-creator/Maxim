class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 50
        self.happiness = 50

    def eat(self):
        self.hunger -= 20
        print(self.name, "поїв. Рівень голоду:", self.hunger)

    def sleep(self):
        self.energy += 30
        print(self.name, "спить. Енергія:", self.energy)

    def play(self):
        self.energy -= 15
        self.happiness += 20
        print(self.name, "грається. Щастя:", self.happiness)

    def status(self):
        print("Кіт:", self.name)
        print("Голод:", self.hunger)
        print("Енергія:", self.energy)
        print("Щастя:", self.happiness)


cat1 = Cat("Барсик")

cat1.status()
cat1.eat()
cat1.play()
cat1.sleep()
cat1.status()
