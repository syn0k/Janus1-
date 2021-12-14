# yield

def next_number():
    for x in [1, 2, 3, 4, 5, 6]:
        yield x


a = next_number()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
