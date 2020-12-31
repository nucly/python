from random import randint
import sys

a = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    x = int(input('put a number between 1 - 10'))
    try:
        if 0 < x < 11:
            if x == a:
                print('correct!')
                break
        else:
            print('has to be 1-10')
    except ValueError:
        print('enter a number')
        continue