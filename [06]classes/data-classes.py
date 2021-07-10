#--------##--------##--------##--------##--------##--------##--------##--------#

# Data Classes

# So far, we've learned that we can use classes to store data and functionality
# within one so-called 'bundle'.

# In the future we may come across classes that only store data:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Let's create 2 'Point' objects, and compare them:
p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)
'''
RESULT: False
'''

# Why is this false? By default, Python compares objects based on their
# location in memory (we know this). If two variables are referenced in the
# same object in memory, they're considered equal. In this example, our two
# 'Point' objects are in two different locations, even though they have the
# exact same attributes.

# To prove this, we can call the 'id' function - this function will tell us
# an object's address within memory:
print(id(p1))
print(id(p2))
'''
RESULT:
4404429248
4404429776
'''
# As you can see - two different locations!
# To solve this, we can define a method within our class called '__eq__':


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)
'''
RESULT: True
'''
# The problem is solved! But, writing all that code is a bit tedious.
# When dealing with classes that contain only data, instead of explicitly
# calling a 'magic method' (__eq__), we can use a 'namedtuple' instead.
# NOTE: Continued in part 2
