# Every function in Python returns a value. Even if there is no return value the function will return None.
# Every function start with def.
# In Python you never specify the datatype of anything. Python keeps track of it.
# Functions arguments can have default value.
# You can't use unnamed argument after name argument in the function. After each named argument you should follow it
# with another named argument

def multiply(a):
    ''' Multiply stuff '''
    return a * 1


def multiply_by(a, b=2):
    return a * b


if __name__ == '__main__':
    print(multiply_by(2, 4))
    print(multiply(2))
