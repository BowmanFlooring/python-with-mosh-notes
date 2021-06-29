#-------------------------------------------------------------------------------

# Generator Expressions

# EX:
values = [x * 2 for x in range(10)]
for x in values:
    print(x)
'''
RESULT:
0
2
4
6
8
10
12
14
16
18
'''

# If we switch out the square brackets for parentheses, our list comprehension
# expression now becomes a 'generator object'. This means that it will NOT
# store the value of every iteration in memory - only the last, or current,
# iteration's value. This would be useful with objects in the 10,000+ range.

# We can get the size of an object by importing 'getsizeof' from the 'sys'
# module:
from sys import getsizeof
# Then, using the getsizeof method, with our list passed in as the argument:
values = (x * 2 for x in range(100000))
print(getsizeof(values))
# SIZE = 112 Bytes
values = (x * 2 for x in range(100))
print(getsizeof(values))
# SIZE = 112 Bytes

# This could potentially prove to be a very useful tool.
# NOTE: Because of the nature of a generator object's structure, we CANNOT
# obtain one's length. Python will throw us an error. So we WILL NOT KNOW
# ahead of time how many objects, or items, this generator object will produce.
