spisok = [16, 46, 26, 36]
for i in enumerate(spisok):
    print(i)
# (0, 16) # (1, 46) # (2, 26) # (3, 36)

b = "hello"
for i in enumerate(b):
    print(i)
# (0, 'h') # (1, 'e') # (2, 'l') # (3, 'l') # (4, 'o')

# Эти кортежи можно распаковывать, то есть извлекать индекс и значение, в теле цикла:
for item in enumerate(spisok):
    print(item[0], item[1])

# 0 16 # 1 46 # 2 26 # 3 36

# Однако чаще это делают еще в заголовке for, используя две переменные перед in:
for id, val in enumerate(spisok):
    print(id, val)

# 0 16 # 1 46 # 2 26 # 3 36

