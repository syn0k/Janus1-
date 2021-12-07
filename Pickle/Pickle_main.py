import pickle

class Character:
    def __init__(self, race, damage=10):
        self.race = race
        self.damage = damage
        self.health = 100

    def hit(self, damage):
        self.health -= damage

    def is_dead(self):
        return self.health == 0

c = Character("Elf")
c.hit(10)
print(c.health)

with open(r"c:\test.bin", "w+b") as f:
    pickle.dump(c, f)

