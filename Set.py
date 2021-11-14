# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data,
# the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed.


# Set Methods
# Python has a set of built-in methods that you can use on sets.
#
# Method	Description
# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others

# create set
myset = {"apple", "banana", "cherry"}

print(f'Print set {myset}')
print(f'Print type set {type(myset)}')

# aad to set data
myset.add('car')  # TypeError: set.add() takes exactly one argument (2 given) :)
print(f'Print set {myset}')

# when adding a non-unique value, this is what happens :)
myset.add('car')
print(f'Print set {myset}')

# remove item
myset.remove('car')
print(f'Print set {myset}')

# Check the item
print('car' in myset)

# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# isdisjoint()	Returns whether two sets have a intersection or not
set1 = {1, 2, 3, 4, 5, 6, 7, 8}
set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
set3 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
print(f'Print issubset - {set1.issubset(set2)}')
print(f'Print issuperset - {set2.issuperset(set1)}')
print(f'Print isdisjoint - {set2.isdisjoint(set1)}')

# union()	Return a set containing the union of sets
# intersection()	Returns a set, that is the intersection of two other sets
# difference()	Returns a set containing the difference between two or more sets
print(f'Print onion {set1.union(set2)}')
print(f'Print intersection - {set1.intersection(set2)}')
set1.difference(set3)
print(f'Print difference - {set1}')

# update()	Update the set with the union of this set and others
set1.update(set2)
print(f'Print update - {set1}')
