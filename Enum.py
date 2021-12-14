from enum import Enum


# Example 1
class Weapon(Enum):
    SWORD = 1
    BOW = 2
    DAGGER = 3
    CLUB = 4


ranged_weapon = Weapon.BOW
print(ranged_weapon)

if ranged_weapon == Weapon.BOW:
    print("It's a bow")

print(list(Weapon))

# Example 2
Weapon = Enum('Weapon', 'SWORD BOW DAGGER CLUB', start=10)

for weapon in Weapon:
    print(weapon)

for weapon in Weapon:
    print(weapon.name, weapon.value)
