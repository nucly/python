import os, glob, time

print(os.getcwd())

path = os.path.join('/Users/dariuszkaminski/PycharmProjects/diveIntoPython3/examples', 'test.py')
print(path)

path = os.path.expanduser('~')
print(path)

path = os.path.join(os.path.expanduser('~'), 'diveIntoPython3')
print(path)

# Splitting the path

pathname = '/Users/dariuszkaminski/PycharmProjects/diveIntoPython3/examples/test.py'
(dirname, filename) = os.path.split(pathname)
print(dirname + ' / ' + filename)

(filename, ext) = os.path.splitext(filename)
print(filename + ' ' + ext)

# Listing directories

d_list = glob.glob('*.py')
print(d_list)

d_list = glob.glob('*list*.py')
print(d_list)

# Metadata
metadata = os.stat('1. lists.py')
print(time.localtime(metadata.st_mtime))
print(metadata.st_size)

print(os.path.realpath('1. lists.py'))





