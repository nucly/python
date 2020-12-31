import re

string = 'search inside the string'
pattern = re.compile('the')
r = pattern.search(string)
print(r)