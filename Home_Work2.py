# Build a cycle from 0 to the entered number inclusively and calculate the sum of all numbers,
# divisible by 3 and 5 without a remainder, print this number to the console.
# Note:
# The task is solved both by direct 'for' and by using List Comprehension
# (you can sum the numbers of the "filtered" list by passing the list to the sum (arg_list) function)
# *********************************'#My decision, task 3'*************************
print('#My decision, task 3')
try:
    PleaseInput_int = int(input('Please input the number\n'))
    arg_list = []
    for x in range(PleaseInput_int + 1):
        if x % 3 == 0:
            # print(f'3 {x}') debug
            arg_list.append(x)
        elif x % 5 == 0:
            # print(f'5 {x}') debug
            arg_list.append(x)
    # print(arg_list) #debug
    print(f'Summa - {sum(arg_list)}')
except ValueError:
    print("That's not an int!\nPlease input the number\n")

#************************************'#Teacher''s decision, task 3'**************
print('#Teacher''s decision, task 3')
try:
    PleaseInput_int = int(input('Please input the number\n'))
    arg_list = []
    for x in range(PleaseInput_int + 1):
        if x % 3 == 0 or x % 5 == 0:
            arg_list.append(x)

    print(f'Summa - {sum(arg_list)}')
except ValueError:
    print("That's not an int!\nPlease input the number\n")
# ********************************************************************************
print('#Teacher''s decision part 2, task 3')
PleaseInput_int = int(input('Please input the number\n'))
arg_list = sum([x for x in range(PleaseInput_int + 1) if x % 3 == 0 or x % 5 == 0])
print(f'Summa - {arg_list}')
# ********************************************************************************


# The input is two lists of numbers of length N.
# Problem: Take all odd numbers from the first list,
# from the second even ones and combine them in a new list called joiner_list.

#
first_lst = 10
second_lst = 10
arg_list1 = []
arg_list2 = []
joined_list = []
for x in range(first_lst + 1):
    if x % 2 == 0:
        # print(f'3 {x}')
        arg_list1.append(x)

for x in range(second_lst + 1):
    if x % 2 == 0:
        print(f'2 {x}')
    else:
        # print(f'3 {x}')
        arg_list2.append(x)

joined_list = arg_list1 + arg_list2

print(joined_list)  # debug
#print(f'{joiner_list}')
