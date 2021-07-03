# -------------------------------------------------------------------------------

# Magic Methods

# If you google 'python 3 magic methods', the first result is a pretty large-
# sized webpage with full in-depth breakdowns of all 'magic methods'. Read it.

class Point:
    # Here's a 'magic method':
    # This, and many other magic methods, are already assigned as methods to 
    # classes we create in Python. 
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

# On the webpage referenced above, the '__str__(self)' method is as follows:
# "Defines behavior for when 'str()' is called on an instance of your class"
# So, we define this 'point' variable, and it in we are storing our 'Point'
# object....  Let's print our variable and see what we get:

point = Point(1, 2)
print(point)
'''
RESULT:
<__main__.Point object at 0x107edafa0>
'''
# This returns the name of our module, followed by the class name, then the 
# address of this point object in memory

# NOTE: THIS IS THE DEFAULT IMPLEMENTATION OF THE '__str__' METHOD IN OUR
# POINT OBJECT.

# Not only do we have the '__str__' magic method, but if we type
# 'point.' and look at the completion:
'''
point.draw
point.__annotations__
point.__class__
point.__delattr__
point.__dict__
point.__dir__
point.__doc__
point.__eq__
point.__format__
point.__getattribute__
point.__hash__
point.__module__
point.__init__
point.__init_subclass__
point.__ne__
point.__new__
point.__reduce__
point.__reduce_ex__
point.__repr__
point.__setattr__
point.__sizeof__
point.__slots__
point.__str__
'''
# We DID NOT explicitly create these class methods. Our class has inherited
# them from another object via a process call 'inheritence'. We will learn
# all about 'inheritence' in a later lecture.

# So, back to our class from above:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Let's define another class-level attribute right here. For the example,
    # we will use the '__str__' magic method.
    # NOTE: THIS WILL CHANGE THE DEFAULT IMPLEMENTATION OF '__str__' to the
    # formatted string we have just defined within the our 'Point' class.
    # This is super important, and super powerful, conceptually. 
    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(point)
'''
RESULT:
(1, 2)
'''

# There are so many possibilities with JUST THOSE TWO magic methods. In the
# following lectures, we will learn about quite a few more.
