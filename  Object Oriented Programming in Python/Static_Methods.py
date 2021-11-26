# Static Methods - @staticmethod, @classmethod

class StaticTest:
    x = 1

t1 = StaticTest()
print(f'Instanse {t1.x}')
print(f'class {StaticTest.x}')

t1.x = 2
print(f'Instanse {t1.x}')
print(f'class {StaticTest.x}')

StaticTest.x=3
print(f'Instanse {t1.x}')
print(f'class {StaticTest.x}')

print(type(t1.x))
print(type(StaticTest.x))



class Person:
    @staticmethod
    def is_adult(age):
        if age > 18:
            return True
        else:
            return False

print(Person.is_adult(23))