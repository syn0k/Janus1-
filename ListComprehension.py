# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
#
# Example:
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
print(type(newlist))
