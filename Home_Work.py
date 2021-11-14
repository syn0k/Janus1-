# # Home Work
# Output the asterisk symbol by a ladder by the number of lines specified by the user:
# ask the user to enter the number of lines, display the asterisks with a ladder.
#
# - For example, the user entered the number 2. Then we output:
# *
# **

print('#My decision, task 1')
try:
    PleaseInput_int = int(input('Please input the number\n'))
    ch = ''
    x = 0
    while x < PleaseInput_int:
        x += 1
        ch += "*"
        print(ch)
except ValueError:
    print("That's not an int!\nPlease input the number\n")

print('#Teacher''s decision, task 1')
PleaseInput_int = int(input('Please input the number\n'))
for x in range(PleaseInput_int):
    print('*' * (x + 1))

# Prompt the user to enter a number. Construct a cycle from 0 to the entered number (inclusive)
# and for even numbers output that they are even, and for odd ones that they are odd. Output example:
# 0 is EVEN
# 1 is ODD
# 2 is EVEN
# etc...
print('#My decision, task 2')
try:
    PleaseInput = input('Please input the number, We will check even or odd  \n')
    # debug print(type(PleaseInput))
    PleaseInput_int = int(PleaseInput)
    # debug print(type(PleaseInput_int))

    x = 0
    while x < PleaseInput_int:
        if x % 2 == 0:
            print(f'{x} is EVEN')
        else:
            print(f'{x} is ODD')
        x += 1

except ValueError:
    print("That's not an int!\nPlease input the number\n")

print('#Teacher''s decision, task 2')
PleaseInput_int = int(input('Please input the number\n'))
for x in range(PleaseInput_int + 1):
    if x % 2 == 0:
        print(f'{x} is EVEN')
    else:
        print(f'{x} is ODD')
