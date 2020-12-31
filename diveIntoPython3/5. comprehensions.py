import glob, os

# A list comprehension provides a compact way of mapping a list into another list by applying a function to each of the
# elements of the list.

a_list = [1, 2, 3, 4]
print(a_list)

b_list = [elem * 2 for elem in a_list]
print(b_list)

paths = [os.path.realpath(f) for f in glob.glob('*.py')]
for p in paths:
    print(f'{p} \n')


paths = [f for f in glob.glob('*.py') if os.stat(f).st_size > 200]
print(f'{paths} \n')

# Creates list of tuples
paths = [(os.stat(f).st_size, os.path.realpath(f)) for f in glob.glob('*.py')]
for p in paths:
    print(p)

# Dictionary comprehension
metadata_dict = {f:os.stat(f) for f in glob.glob('*list*.py')}
print(metadata_dict.keys())