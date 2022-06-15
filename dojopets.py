class Ninja: 
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet


    def Walk(self):
        print("let's walk!")
        self.pet.play()
        return self
    def Feed(self):
        print("Time to eat")
        self.pet.eat()
        return self
    def Bathe(self):
        print("time for a bath")
        self.pet.noise()
        return self


class Pet(Ninja):
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 20
        self.energy = 20
        self.noise = noise
    def sleep(self):
        self.energy += 25
        return self
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    def play(self):
        self.health += 5
        return self
    def noise(self):
        print(self.noise())
    def show_stats(self):
        print(f"Health: {self.health}")
        print(f"Energy: {self.energy}")

Doggo = Pet("doggo", "dog", "sit", "bork")
Owner1 = Ninja("Emmet", "Allen", "biscuits", "kibble", Doggo)


Owner1.Walk().Feed()
Doggo.sleep().show_stats()
