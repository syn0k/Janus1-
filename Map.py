# # MAP
def print_me(age):
    return age*age

numbers = [1,2,3,4,5]
for x in map(print_me, numbers):
    print(x)

qwe = map(print_me, numbers)
print(type(qwe))
print(list(map(print_me, numbers)))

# Filter

def is_adult(agee):
    return agee >= 18
    #return True or False

age1 = [14, 19, 20, 25]
filter(is_adult, age1)
print(list(filter(is_adult, age1)))


#Lambda
age = [14, 19, 20, 25]
lbd = lambda age: age >= 18
print(list(filter(lbd, age)))

#example
list(filter(lambda age: age >= 18, age))

multi = lambda x,y: x*y
multi(2,3)
print(multi(2,3))








