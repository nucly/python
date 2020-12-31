a_list = ['a', 'b', 'b', 'c', 'd']

# There are 4 ways to add to the list

a_list = a_list + [20, 'darek']
print(a_list)

a_list.append(1.0)
print(a_list)

a_list.extend(range(2))
print(a_list)

a_list.insert(0, True)
print(a_list)

# Searching for values in a list

x = a_list.count('b')
print(x)

x = 'b' in a_list
print(x)

x = a_list.index('c')
print(x)

# Removing items from a list

del a_list[0]
print(a_list)

a_list.remove('a')
print(a_list)

x = a_list.pop()
print(x)

x = a_list.pop(1)
print(x)

