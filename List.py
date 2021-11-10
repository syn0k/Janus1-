# List collection
# Python Lists
# Python Lists
# Access List Items
# Change List Items
# Add List Items
# Remove List Items
# Loop Lists
# List Comprehension
# Sort Lists
# Copy Lists
# Join Lists

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list


n = 0
int_list = [1, 32, 35, 41, 59, 65, 73, 822, 922, 101]
mixed_list = [1, 2.0, 'string', 4, "more", 6, 7, 'HelloWorld', 9, 10]

big_list = mixed_list + int_list
print(f'Print big list {big_list}')

big_list.append('HelloWord2')
print(f'Print big list add {big_list}')

big_list.pop(-1)
print(f'Print big list pop -1 {big_list}')

big_list.pop(1)  # index = 1
print(f'Print big list pop index 1  {big_list}')

int_list.sort()
print(f'Print sort {int_list}')

thislist = [1, 2.0, 'string', 4, 'more', 6, 7, 'HelloWorld', 9, 10, 1, 32, 35, 41, 59, 65, 73, 822, 922, 101,
            'HelloWord2']
if 'HelloWorld' in thislist:
    print("Yes, HelloWorld")

print(len(int_list))
print(len(mixed_list))

print(int_list[3])
print(mixed_list[2])

for entry in mixed_list:
    n += 1
    print(f"{n}. {mixed_list}")

n = 0
for entry in mixed_list:
    n += 1
    print(f"{n}. {entry}")
