import random

#
# print('#Teacher''s decision, task 7')
# number = int(input('Enter the number\n'))
#
# reversed_number = 0
# tmp_original = number
# while tmp_original > 0:
#     reversed_number = (reversed_number*10) + tmp_original % 10
#     print(reversed_number)
#     print(tmp_original)
#
#     tmp_original = tmp_original // 10
#
# if number == reversed_number:
#     print('Palindrome')
# else:
#     print('Np Palindrome')


# The computer guesses a number from 1 to 50 and gives 6 attempts to the user so that he can guess the guessed number.
# When the user enters a number, the computer checks whether the number is guessed and,
# if not guessed, then reports whether the guessed number is less or more.
# If the user guessed it, it informs that the number is guessed.
# print('#My decision, task 8')
rnd_int = random.randint(1, 50)
input_count = 1
while input_count < 7:
    print(f"You have 6 attempts, now the {input_count} attempts")
    input_number = int(input('Enter the interval number range 1 - 50\n'))

    input_count += 1
    if input_number in range(1, 9):
        if input_number == rnd_int:
            print(f"You Wins {rnd_int}'")
            break
        else:
            print(f"closer {rnd_int}'")
    elif input_number in range(10, 19):
        if input_number == rnd_int:
            print(f"You Wins {rnd_int}'")
            break
        else:
            print(f"closer {rnd_int}'")
    elif input_number in range(20, 29):
        if input_number == rnd_int:
            print(f"You Wins {rnd_int}'")
            break
        else:
            print(f"closer {rnd_int}'")
    elif input_number in range(30, 39):
        if input_number == rnd_int:
            print(f"You Wins {rnd_int}'")
            break
        else:
            print(f"closer  {rnd_int}'")
    elif input_number in range(40, 50):
        if input_number == rnd_int:
            print(f"You Wins {rnd_int}'")
            break
        else:
            print(f"closer {rnd_int}'")
    else:
        print("The number is not included in the interval  ")

print('#Teacher''s decision, task 8')
number = random.randint(1, 50)
trues = 0
while trues < 6:
    guess = int(input('Enter the interval number range 1 - 50\n'))
    trues += 1
    if trues < guess:
        print("too low")
    if trues > guess:
        print("too high")
    if trues == guess:
        print("You Wins")
        break
    if number != guess and trues == 6:
        print(f"Sorry, but you dont't make it. My number was: {rnd_int}")
        break
