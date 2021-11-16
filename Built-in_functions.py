as1=abs(-1)
print(as1)


mx = max(1,2,3,4,5,6,7,8,9,10)
mn = min(1,2,3,4,5,6,7,8,9,10)
print(mn, mx)

pw = pow(2,8)
print(pw)

r_ = round(3.1415,2)
print(r_)

s_ = sum([1,2,3,4,5])
print(s_)

hs= hex(42) #16
os = oct(42) #0o 6
bs = bin(42) # 0b bin
print(hs)
print(os)
print(bs)


all_true1 = all([True, True, True])
all_true2 = all([True, False, True])
print(all_true1)
print(all_true2)

namedcars = [('car1', 1999), ('car2', 2002), ('car3', 1990)]
qq=all(name1 > 1999 for _, name1 in namedcars)
print(f'All {qq}')

any_1 = any([True, False, False])
any_2 = any([False, False, False])
print(any_1)
print(any_2)

ler= 'ajhf'
numbers = (10,20,30)
zipped = zip(ler, numbers)
print(type(zipped))
print(zipped)

zipped_list = list(zipped)
print(zipped_list)






