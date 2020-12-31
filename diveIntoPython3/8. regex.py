import re

pattern = '''
    ^                   # beginning of string
    M{0,3}              # thousands - 0 to 3 Ms
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                        #            or 500-800 (D, followed by 0 to 3 Cs)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                        #        or 50-80 (L, followed by 0 to 3 Xs)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
                        #        or 5-8 (V, followed by 0 to 3 Is)
    $                   # end of string
    '''

# ^ beginning of the string / $ end of the string
# use raw strings with regex r' '

s = '103 POPLAR ROAD FLAT 3'
reg = re.sub(r'\bROAD\b', 'RD.', s)
print(reg)
print(re.search(pattern, 'M', re.VERBOSE))
print(re.search(pattern, 'MM', re.VERBOSE))
print(re.search(pattern, 'MMM', re.VERBOSE))
print(re.search(pattern, 'MMMM', re.VERBOSE))
print(re.search(pattern, '', re.VERBOSE))
print(re.search(pattern, 'MCM', re.VERBOSE))

pattern2 = '^c{1,3}$'
print(re.search(pattern2, 'c'))
print(re.search(pattern2, 'cc'))
print(re.search(pattern2, 'ccc'))
print(re.search(pattern2, ''))
print(re.search(pattern2, 'cccc'))

phonePattern = re.compile(r"(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$")

# in production you should not chain search and group as
# below because if it won't match you gonna get an exception
print(phonePattern.search('800-555-3331').groups())
print(phonePattern.search('(800)5551212 ext. 1234').groups())
print(phonePattern.search('work 1-(800) 555.1212 #1234').groups())

# ^ matches the beginning of a string.
# $ matches the end of a string.
# \b matches a word boundary.
# \d matches any numeric digit.
# \D matches any non-numeric character.
# x? matches an optional x character (in other words, it matches an x zero or one times).
# x* matches x zero or more times.
# x+ matches x one or more times.
# x{n,m} matches an x character at least n times, but not more than m times.
# (a|b|c) matches exactly one of a, b or c.
# (x) in general is a remembered group. You can get the value of what matched by using the groups() method of the object
# returned by re.search.



