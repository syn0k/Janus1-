def count_vowels(txt):
    return sum([1 for x in txt.lower() if x in 'aeiouy'])


print(count_vowels('BlAblabla'))
print(count_vowels('abcdef'))
print(count_vowels('bcd'))







