# Constants. Protected and private attributes. Properties.

# Example: Public Attributes
# class Student:
#     schoolName = 'XYZ School' # class attribute
#
#     def __init__(self, name, age):
#         self.name=name # instance attribute
#         self.age=age # instance attribute

# Example: Protected Attributes
# instance variable protected is to add a prefix _ (single underscore)
# class Student:
#     _schoolName = 'XYZ School'  # protected class attribute
#
#     def __init__(self, name, age):
#         self._name = name  # protected instance attribute
#         self._age = age  # protected instance attribute
# class
class Character:
    # _ protect
    # __ private
    # const UPPER, class attribute. Character.MAX_SPEED
    MAX_SPEED = 100
    dead_health = 0

    def __init__(self, race=str(50), damage=int(10)):  # class object
        self.damage = damage
        self.__race = race  # __Private
        self._health = 100  # _protect
        self._current_speed = 20  # _protect

    def hit(self, damage):
        self._health -= damage

    @property
    def health(self):
        return self._health

    @property
    def race(self):
        return self.__race

    @property
    def current_speed(self):
        return self._current_speed

    # property
    @current_speed.setter
    def current_speed(self, current_speed):
        if current_speed < 0:
            self._current_speed = 0
        elif current_speed > 100:
            self._current_speed = 100
        else:
            self._current_speed = current_speed


c = Character("Elf")
print(c.current_speed)  # current value
c.current_speed = 50
print(c.current_speed)
c.current_speed = 1000
print(c.current_speed)
