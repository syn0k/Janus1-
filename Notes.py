import random

city_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
print("Выбор случайного города из списка - ", random.choice(city_list))

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
