#Attributes and Methods

class Character(): # class
    max_speed =100
    dead_health=0

    def __init__(self, race= str(50), damage=int(10), armor=int(20)): # class object
        self.race=race
        self.damage = damage
        self.armor = armor
        self.health = 100

    #method
    def hit(self, damage):
        self.health-=damage

    def is_dead(self):
        return self.health==Character.dead_health

unit = Character("Ork")
print(unit.race)
print(Character.max_speed)

unit.hit(20)
print(unit.health)
print(unit.is_dead())
unit.hit(80)
print(unit.is_dead())

