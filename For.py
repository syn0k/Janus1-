# Python For Loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages,
#   and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
import random
set1 = {1, 2, 3, 4, 5, 6, 7, 8}
set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}

# Example
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9] but :)

for x in numbers:
    print(numbers)  # we have [1, 2, 3, 4, 5, 6, 7, 8, 9] but :)

for x in numbers:
    print(x)  # we have 1,2,3,4,5,6,7,8,9 how a new line :) great

# example is more complicated
# set1 = {1, 2, 3, 4, 5, 6, 7, 8} primary numbers
# set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11} secondary numbers

# primary
for x_set1 in set1:
    print(f"Primary numbers - {x_set1}")
    # secondary
    for x_set2 in set1:
        print(f"Secondary numbers- {x_set2}")

# range( begin, end, step)
next = range(0, 100, 2)
for x in next:
    print(x)

# Just fo fan
# print a random item from 'set_city' where we have a space
set_city = ['Anacortes (1961)', 'Bellevue (1955, 2021)', 'Bellingham (1980)', 'Chewelah (1972)',
            'Everett (2002)', 'Leavenworth (1967)', 'Olympia (1987)', 'Port Angeles (1953)',
            'Richland (1960)', 'Seattle (1959, 1966)', 'Seattle and S. King Co. (2012)',
            'Spokane (1975, 2004, 2015)', 'Tacoma (1956, 1984, 1998)', 'Vancouver (1957, 1987)',
            'Yakima (1994, 2015)', 'Bluefield (1964)', 'Clarksburg (1957)', 'Grafton (1962)']
string_text = 'Just fo fan'
for entry in string_text:
    if entry == " ":
        print(random.choice(set_city))
    else:
        print(entry)

city = [('Anacortes', 1961), ('Bellevue', 2021), ('Bellingham', 1980), ('Chewelah', 1972)]
for (name, year) in city:
    print(f'Founding of the city of {name}, in  {year} year')
