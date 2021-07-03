#-------------------------------------------------------------------------------

# Class vs. Instance Methods

# In the last lecture, we learned about 'class vs. instance attributes'
# We have the same concept around 'methods' that we do when defining attributes
# of a class:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Here's where we will start:
    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

# Now, let's call this method to test it out:
point = Point.zero()
point.draw()
'''
RESULT:
Point (0, 0)
'''
