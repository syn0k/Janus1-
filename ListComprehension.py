# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
#
# Example:
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

# this is standart method
for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)  # but there is a shorter and more compact

# List Comprehension
# The Syntax
# newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

word = "Hello World"  # curent string
word2 = []  # new string for List Comprehension
for c in word:
  word2.append(c)
  print(c)

print(word2)

LComprehension = [l for l in word]
print(LComprehension)

# In the following example, we introduce a new condition element(if)
LComprehension = [l for l in word if l != 'l']
print(LComprehension)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)

numbers = [n for n in range(0, 11)]
print(numbers)

numbers = [n * n for n in range(0, 11)]
print(numbers)

numbers = [n * n for n in range(0, 11) if n % 2 != 0]
print(numbers)

# translate sentiment into inches
new_sen = [12, 22, 11, 32]
inc = [round(x / 2.54, 2) for x in new_sen]
print(f'We have 12,22,11,32 sentiment')
print(f'Print result inches - {inc}')
