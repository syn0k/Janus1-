# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
#
# Syntax
# lambda arguments : expression

x = lambda a: a + 10
print(x(5))

x = lambda a, b: a * b
print(x(5, 6))


def square(number):
    return number*number

numbers = [1,2,3,4,5,6,7]
pr_sq=map(square, numbers)
print(pr_sq)

for x in map(square, numbers):
    print(x)

pr_list=list(map(square, numbers))
print(pr_list)


def f_age(age):
    return age >= 18

age = [17,18,11,20]
pr_age=list(filter(f_age, age))
print(pr_age)

#Lambda example

ages = [17, 18, 11, 20]
p = lambda age1: age1 >= 18
print(list(filter(p, ages)))



