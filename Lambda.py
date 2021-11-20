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

