# Python Loops
# Python has two primitive loop commands:
# while loops
# for loops
#
# The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.
#
# Example
# Print i as long as i is less than 6:

i = 1
while i < 6:
    print(i)
    i += 1

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
