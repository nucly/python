import glob, os, time, re

# 1. Simple function with one param
def multiply(a):
    pass

# 2. Function with default param
def multiply(a, b=2):
    pass

# 3. a_list
a_list = ['word', 20]
a_list.append(1.0)
a_list.insert(0, True)
a_list.count('word')
a_list.index('word')
a_list.remove('word')
a_list.pop()
a_list.pop(1)
del a_list[0]
'word' in a_list

# 4. Tuples
tuple = (1,2,3)
(x,y,z) = tuple
(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(1, 8)
print(MONDAY)

# 5. a_sets / unique values
a_set = {1,2}
a_set = set([1,2,3])
a_set = set()
a_set.add(1)
a_set.update({3,4,5})
a_set.update([6,7,8])
a_set.discard(7) # no exceptions
a_set.remove(4) # exception if no value
a_set.pop() # random pop
2 in a_set
b_set = {'a', 'b', 'c', 'd'}
c_set = a_set.union(b_set)

a_set = {'a', 'c', 'b'}
b_set = {'a', 'b', 'c', 'd', 'e', 'f'}
a_set.intersection(b_set)
b_set.difference(a_set)
b_set.symmetric_difference(a_set)
a_set.issubset(b_set)
a_set.issuperset(b_set)
b_set.issuperset(a_set)

# 6. Dictionaries
a_dict = {'database': 'mysql', 'port': 3020}
a_dict['database']
a_dict['database'] = 'sqlite'
a_dict['user'] = 'dazza'

SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

1000 in SUFFIXES
len(SUFFIXES)
SUFFIXES[1000][3]

# 7. Comprehensions
# A list comprehension provides a compact way of mapping a list into another
# list by applying a function to each of the elements of the list.

a_list = [1, 2, 3, 4]
b_list = [elem * 2 for elem in a_list]

paths = [os.path.realpath(f) for f in glob.glob('*.py')]
for p in paths:
    print(f'{p} \n')

paths = [f for f in glob.glob('*.py') if os.stat(f).st_size > 200]

paths = [(os.stat(f).st_size, os.path.realpath(f)) for f in glob.glob('*.py')]
for p in paths:
    print(p)

metadata_dict = {f:os.stat(f) for f in glob.glob('*list*.py')}
print(metadata_dict.keys())

# 8. File I/O
path = os.path.join('/Users/dariuszkaminski/PycharmProjects/diveIntoPython3/examples', 'test.py')
print(path)

path = os.path.expanduser('~')
print(path)

path = os.path.join(os.path.expanduser('~'), 'diveIntoPython3')
print(path)

pathname = '/Users/dariuszkaminski/PycharmProjects/diveIntoPython3/examples/test.py'
(dirname, filename) = os.path.split(pathname)
(filename, ext) = os.path.splitext(filename)

d_list = glob.glob('*.py')
d_list = glob.glob('*list*.py')

# Metadata
metadata = os.stat('1. lists.py')
print(time.localtime(metadata.st_mtime))
print(metadata.st_size)
print(os.path.realpath('1. lists.py'))

# 9. Strings
username = 'mark'
password = 'sialalal'
print('{0} + {1}'.format(username, password))

a_list = [1, 2, 3, 4]
print('{0[0]} + {0[1]}'.format(a_list))

x = 625.55
print('{0:.1f}'.format(x))

a_string = 'Hello World'
print(a_string[6:])

by = b'abcd\x65'
print(by[0])

barr = bytearray(by)
barr[0] = 102
string_to_bytes = a_string.encode('utf-8')
bytes_to_string = string_to_bytes.decode()

# 10. Generators
def make_counter(x):
    print('entering make_counter')
    while True:
        yield x
        print('incrementing x')
        x += 1

counter = make_counter(2)
print(next(counter))
print(next(counter))
print(next(counter))

def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)

    def apply_rule(word):
        return re.sub(search, replace, word)

    return matches_rule, apply_rule

def rules(rules_filename):
    with open(rules_filename, encoding='utf-8') as pattern_file:
        for line in pattern_file:
            pattern, search, replace = line.split(None, 2)
            yield build_match_and_apply_functions(pattern_file, search, replace)

def plural(noun, rules_filename='9. plural_rules'):
    for matches_rule, apply_rule in rules(rules_filename):
        if matches_rule(noun):
            return apply_rule(noun)
    raise ValueError('no matching rule for {0}'.format(noun))

# 11. 
