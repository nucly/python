from collections import Counter, defaultdict, OrderedDict
import datetime
import pdb
from array import array

pdb.set_trace()
li = [1, 2, 3, 4, 5,]

dictionary = defaultdict(lambda : 5, {'a': 1, 'b': 2})
print(dictionary['c'])

d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

print(d2 == d)

d = array('i', [1, 2 ,3])
print(d[0])
