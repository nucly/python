a_set = {1, 2}
print(a_set)

a_list = [1, 2, 3, 4]
a_set = set(a_list)
print(a_set)

# You can't create an empty set with {} as this would be a dictionary
# Use set() instead
a_set = set()
print(a_set)

# Sets have unique values, adding the same value won't do anything
a_set.add(1)
a_set.add(2)
a_set.add(1)
print(a_set)

a_set.update({4, 5, 6})
a_set.update([7, 8, 9])
print(a_set)

# No exceptions if the value does not exist
a_set.discard(7)
print(a_set)

# If you will try to .remove() when the value does not exist the KeyError exception will raise
a_set.remove(4)
print(a_set)

# Random item will be removed with pop() as sets don't have the "last" value
a_set.pop()
print(a_set)

print(2 in a_set)

b_set = {'a', 'b', 'c', 'd'}
new_set = a_set.union(b_set)
print(new_set)

a_set = {'a', 'c', 'b'}
b_set = {'a', 'b', 'c', 'd', 'e', 'f'}

print(a_set.intersection(b_set))
print(b_set.difference(a_set))
print(b_set.symmetric_difference(a_set))

print(a_set.issubset(b_set))
print(a_set.issuperset(b_set))
print(b_set.issuperset(a_set))




