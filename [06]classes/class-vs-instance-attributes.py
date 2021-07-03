#-------------------------------------------------------------------------------

# Class vs. Instance Attributes

# So, last lecture, we learned we can define attributes for our 'Point' object in
# the 'constructor' of the 'Point' class. Now, by default, whenever we create a
# new 'point' object, that 'point' object will have those attributes by default.

# Classes in Python are DYNAMIC - meaning we can ALSO define an attribute AFTER
# we create a 'point' object. Let's pull last lecture's code back up:

class Point:
    def __init__(self, x, y): # <- the 'constructor'
        self.x = x # <- defining an attribute
        self.y = y # <- defining an attribute

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2) # <- creation of our 'point' object
point.z = 10 # <- dynamically defining another attribute
point.draw()
# All attributes we have defined so far are called 'instance attributes'.
# That means these are attributes that belong to point instances - or point
# objects. So every point instance can have different values for all of 
# it's attributes. For example, we already have one point instance {line 21},
# so let's make another, and draw it on the terminal:
another = Point(3, 4)
another.draw()
'''
RESULT:
Point (1, 2)
Point (3, 4)
'''
# These two point objects are completely indepenent of each other. Just like
# John and Mark can have two different eye colors.

# But, we can also define attributes at the class level. 
class Point:
    default_eyecolor = "red" # <- 'class level attribute'
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    
    def draw(self):
        print(f"Point ({self.x}, {self.y})")
 
# That would be like saying 'all humans have two eyes, and two ears'.
# Class level attributes are shared across all instances of a class.
# If we change their value, the change is visible to all objects of that type.

# NOTE: IN MOST CASES, WE WILL BE USING INSTANCE ATTRIBUTES. BUT THERE MAY
# BE TIMES THAT WE MAY WANT TO DEFINE A CLASS LEVEL ATTRIBUTE THAT IS SHARED
# ACROSS ALL OBJECTS OF A GIVEN TYPE.
