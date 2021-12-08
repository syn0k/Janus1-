class Character:
    def __init__(self, race, damage=10):
        self.race = race
        self.damage = damage

    def __eq__(self):
        return f"Character ({self.race}), {self.damage})"

    def __str__(self):
        return f"{self.race} with damage =  {self.damage}"

    def __eq__(self, other):
        if isinstance(other, Character):
            return self.race == other.race and self.damage ==  other.damage

    # # for Python 2
    # def __ne__(self, other):
    #     pass

c = Character("Elf")

