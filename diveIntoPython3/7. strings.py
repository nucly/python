username = 'mark'
password = 'sialalal'
print('{0} + {1}'.format(username, password))

a_list = [1, 2, 3, 4]
print('{0[0]} + {0[1]}'.format(a_list))

# Format specifier
x = 625.55
print('{0:.1f}'.format(x))

# Slicing strings
a_string = 'Hello World'
print(a_string[6:])

# Bytes / b and then ' ' / bytes object is immutable, use bytearray instead
by = b'abcd\x65'
print(by[0])

barr = bytearray(by)
barr[0] = 102
print(barr)

string_to_bytes = a_string.encode('utf-8')
print(string_to_bytes)

bytes_to_string = string_to_bytes.decode()
print(bytes_to_string)