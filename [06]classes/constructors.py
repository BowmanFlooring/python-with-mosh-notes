# Constructors

# If we want to supply initial coordinates to our Point object, we to call
# a method called a 'constructor', which is a special method called when we create
# a new 'Point' object. Here's how to create a constructor:

class Point:
    def __init__(self, x, y):
    # '__init__' is a special method called a 'magic method'. Python classes have
    # several magic methods. Then, we add optional parameters, 'x' and 'y', which
    # will be the coordinates. And 'self' is a reference to the 'Point' object.
    # So, we can use that to set the 'x' and 'y' attributes, like:    
        self.x = x
        self.y = y
        # Now, when we use the dot operator - 'point.' - we have the 'draw' 
        # method, as well as the two new attributes - 'point.x' and 'point.y'.

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
# Let's print, and check out our new attributes:
print(point.x)
print(point.y)
'''
RESULT:
1
2
'''
# Let's check out our 'draw' method now:
point.draw()
'''
RESULT:
Point (1, 2)
'''
