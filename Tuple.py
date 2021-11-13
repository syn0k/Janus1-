# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.


thistuple = (1, 2.0, 'string', 4, 'HelloWord2', 'more', 6, 7, 'HelloWorld', 9, 10, 1, 32, 35, 41, 59, 65, 73, 822, 922,
             101, 'HelloWord2', 1)
print(f'Print tuple  - {thistuple}')
print(f'Len tuple - {len(thistuple)}')
print(f'Print get tuple index - {thistuple[0]}')
print(f'Print the index of a tuple from the end - {thistuple[-1]}')
print(f"Print count tuple - {thistuple.count('HelloWord2')}")
