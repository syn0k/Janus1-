# Write a rock-paper-scissors game against the computer.
# Run the game in an endless loop. Request user input (R for rock, S for scissors, P for paper).
# Generate a random selection of a computer. Display computer selection.
# Determine the winner by displaying the relevant information.
# Ask the user if he wants to repeat the game. If he wants to repeat, he does not want to leave the cycle.
import random

x = 0
rnd = ['R', 'S', 'P']
while x < 1:
    random_choice = random.choice(rnd)
    choice_user = input('Enter R  for rock, S for scissors, P for paper\n')

    if choice_user == random_choice:
        print('You Wins')
        choice_ = input('Do you want to exit the program? y/N\n')

        if choice_.strip() == 'Y' or choice_.strip() == 'y':
            print('By By')
            x = 2
            break
    else:
        print('didn''t please')
        choice_ = input('Do you want to exit the program? Y/n\n')
        if choice_.strip() == 'Y' or choice_.strip() == 'y':
            print('By By')
            x = 2
            break

print('#Teacher''s decision, task 9')
sh_cont = True
while sh_cont:
    pl_ch = input('R/S/P\n').lower()
    if pl_ch not in ['r', 's', 'p']:
        print('Try again')
        continue
    gen = {1: 'r', 2: 's', 3: 'p'}
    comp_ch = gen[random.randint(1, 2)]
    print(f'Comp choise: {comp_ch}')
    win_comb = [{('p', 'r'), ('r', 's'), ('s', 'p')}]
    if pl_ch == comp_ch:
        print("A draw")
    elif (pl_ch, comp_ch) in win_comb:
        print("Player wins")
    else:
        print("Computer wins")
    sh_con = input("Wont to process [y/n]").lower() == 'y'
