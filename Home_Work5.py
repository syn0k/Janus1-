def whos_first(p1, p2):
    diff = p1.find('B') - p2.find('B')
    if diff < 0:
        return 'p1'
    elif diff > 0:
        return 'p2'
    else:
        return 'tie'

def solve_hanoi_tower(discs):
    return 2 ** discs - 1

def calc_dice_scores(lst):
    return sum([a + b for a, b in lst]) if not any([a == b for a, b in lst]) else 0

def any_duplicates(square):
    plain = [i for z in square for i in x]
    return sorted(plain) != [1, 2, 3, 4, 5, 6, 7, 8, 9]

number_of_sticks = 10
player_turn = 1
while number_of_sticks > 0:
    print(f'How many sticks you take? Remainning {number_of_sticks}')
    taken = int(input())

    if taken < 1 or taken > 3:
        print(f'You tried to take {taken}. Allowed to take 1,2,3 sticks')
        continue
    number_of_sticks-=taken
    print(f'Sticks taken: {taken}')
    if


