class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50

    def eat(self):
        self.hunger -= 10
        print(self.name, "поїв. Рівень голоду:", self.hunger)

    def play(self):
        self.hunger += 10
        print(self.name, "грається. Рівень голоду:", self.hunger)


class Human:
    def __init__(self, name, pet):
        self.name = name
        self.pet = pet

    def feed_pet(self):
        print(self.name, "годує", self.pet.name)
        self.pet.eat()

    def play_with_pet(self):
        print(self.name, "грається з", self.pet.name)
        self.pet.play()


# створення об'єктів
pet1 = Pet("Барсик")
human1 = Human("Максим", pet1)

# симуляція
human1.feed_pet()
human1.play_with_pet()