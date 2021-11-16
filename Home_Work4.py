# Write a rock-paper-scissors game against the computer.
# Run the game in an endless loop. Request user input (R for rock, S for scissors, P for paper).
# Generate a random selection of a computer. Display computer selection.
# Determine the winner by displaying the relevant information.
# Ask the user if he wants to repeat the game. If he wants to repeat, he does not want to leave the cycle.
import random

x = 1
while x > 0:
    rnd = ['R', 'S', 'P']
    random.choice(rnd)
    choice_user = input('Enter R  for rock, S for scissors, P for paper\n')

    if choice_exit == 'Y' or choice_exit == 'y':
        break
    elif choice_exit == 'N' or choice_exit == 'n':
        choice_ = input('Do you want to exit the program? Y/N\n')
    else:
        print('You have not entered')
