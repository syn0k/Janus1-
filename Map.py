# MAP
def print_me(age):
    return age*age

numbers = [1,2,3,4,5]
for x in map(print_me, numbers):
    print(x)

qwe = map(print_me, numbers)
print(type(qwe))
print(list(map(print_me, numbers)))

# Filter

def is_adult(age):
    return age >= 18
    #return True or False

age1 = [14,19,19.20]
filter(is_adult, age1)





