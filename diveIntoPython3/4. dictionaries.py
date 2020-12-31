# A dictionary is an unordered set of key-value pairs. When you add a key to a dictionary, you must also add a value for
# that key. (You can always change the value later.) Python dictionaries are optimized for retrieving the value when you
# know the key, but not the other way around.

a_dict = {'database': 'mysql', 'port': 3020}
print(a_dict['database'])

a_dict['database'] = 'sqlite'
print(a_dict)

a_dict['user'] = 'dazza'
print(a_dict)

SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

print(1000 in SUFFIXES)
print(len(SUFFIXES))
print(SUFFIXES[1000][3])