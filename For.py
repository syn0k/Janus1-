# Python For Loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages,
#   and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

set1 = {1, 2, 3, 4, 5, 6, 7, 8}
set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

# Example
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9] but :)

for x in numbers:
    print(numbers)  # we have [1, 2, 3, 4, 5, 6, 7, 8, 9] but :)

for x in numbers:
    print(x)  # we have 1,2,3,4,5,6,7,8,9 how a new line :) great
