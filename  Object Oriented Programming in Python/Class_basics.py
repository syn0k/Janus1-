#Class basics
class Character(): # class

    def __init__(self, race=str(50), damage=int(10), armor=int(20)): # class object
        self.race=race
        self.damage = damage
        self.armor = armor


unit = Character("Elf", 12, 12)
print(unit.race, unit.damage, unit.armor)

