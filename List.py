# List collection
n = 0
int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mixed_list = [1, 2.0, 'string', 4, "more", 6, 7, 'HelloWorld', 9, 10]

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
