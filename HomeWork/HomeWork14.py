def is_full_house(hand):
    return all([hand.count(i) >= 2 for i in hand])

print(is_full_house(["A","A","A","K","K"]))
print(is_full_house(["3","J","J","3","3"]))
print(is_full_house(["10","J","10","10","10"]))
print(is_full_house(["7","J","3","4","2"]))

