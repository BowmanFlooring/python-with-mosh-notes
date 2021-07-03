# Creating Classes

# Let's create a 'Point' class. For classes, we use the 'Pascal' naming
# convention, which states that the first letter of every word be capitalized,
# and no spaces or underscores as separators:
class Point:
    def draw(self):
        print("draw")


point = Point()
print(type(point))
# Now, if we use the dot operator (Point.), we now have our 'draw' method, along
# with a bunch of others we didn't define. These come from another object in
# Python through a method called 'inheritence' - we will discuss later! Let's check
# the results and see what type we get:
'''
RESULT:
<class '__main__.Point'
'''
# '__main__' is the name of our module - again, we will look at later.

# We can also check to see if an object is an instance of a certain class:
print(isinstance(point, Point))
'''
RESULT:
<class '__main__.Point'
True
'''
