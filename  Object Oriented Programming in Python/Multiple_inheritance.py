#Multiple inheritance

#perent class
class Person:
    def can_breathe(self):
        print('I can breathe')

    def can_walk(self):
        print('I can walk')

#sub class
class Doctor(Person):
    def can_cure(self):
        print('HI, I am Doctor')

class Architect(Person):
    def can_build(self):
        print('HI, I am build')

a = Architect()
a.can_walk()
a.can_build()
a.can_breathe()

d = Doctor()
d.can_cure()
d.can_walk()
d.can_breathe()





