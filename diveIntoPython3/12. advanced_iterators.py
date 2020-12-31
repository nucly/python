import re, itertools

a_string = 'A23K4K54L34L53L2L234L5L'

numbers = re.findall('[0-9]+', a_string)
print(numbers)

assert 1 + 1 == 2
# assert 1 + 1 == 3, "1 + 1 does not equal 3"

# generator expressions
unique_characters = {'A', 'B', 'C', 'D', 'E'}

gen = (ord(c) for c in unique_characters)
print(next(gen))

gen = tuple(ord(c) for c in unique_characters)
print(gen)

# --------------------------------------------------------

names = list(open('people.txt', encoding='utf-8'))

# rstrip() strips the string from trailing whitespaces
names = [name.rstrip() for name in names]
print(names)

# sorted() takes key function to sort it in specific order
names = sorted(names, key=len)
print(names)

groups = itertools.groupby(names, len)

for name_lenght, name_iter in groups:
    print(f"Names with {name_lenght} letters")
    for name in name_iter:
        print(name)

# string manipulation


