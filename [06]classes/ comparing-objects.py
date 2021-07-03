#-------------------------------------------------------------------------------

# Comparing Objects

# Let's simplify the code we've been working on in this section:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point = Point(1, 2)
other = Point(1, 2)
print(point == other)
'''
RESULT:
False
'''
# Why is this false??????:
# Well, by default, the 'equality' operator compares the references, or
# addresses, of these two objects in memory. They are two different variables,
# so they have two different memory addresses - this is why it's 'False'

# To fix this problem, we need another 'magic function':

# Looking back at the 'google' search we did in the last lecture, that page
# cites it's own section of magic methods specifically for comparing two
# objects. For this example, we need to use '__eq__'. So, back to our class:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # On the webpage, it state that '__eq__' takes two parameters:
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        # If this expression evaluates to 'True', that means that these two
        # objects are considered equal. Let's jump all the way down and run it:

point = Point(1, 2)
other = Point(1, 2)
print(point == other)
'''
RESULT:
True
'''

# Say we want to perform a 'greater than' comparison - by default, the Point
# object does not support that. So again, we would write a very similar method,
# this time using the '__gt__' magic method:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y
        # NOTE: Python automatically configures the '<' operator, so
        # we don't need to write this entire thing just for '<'.

point = Point(1, 2)
other = Point(1, 2)
print(point == other)
