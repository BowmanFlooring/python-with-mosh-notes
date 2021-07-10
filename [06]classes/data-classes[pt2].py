#--------##--------##--------##--------##--------##--------##--------##--------#

# Data Classes pt. 2 - the "namedtuple"

from collections import namedtuple

# As arguments for 'namedtuple', we will first pass in the name we want to use
# for our type object. Secondly, we pass an array of field names - or attribute
# names. Attributes we want our object to have:
Point = namedtuple("Point", ["x", "y"])
# Notice, our variable name uses 'Pascal' naming convention here, because it
# is representing a type; a new class. Also, instead of simply passing in some
# arbitrary values to our 'Point' objects - like (1, 2) - we will pass in
# keyword arguments.
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)

# BEWARE: These 'namedtuple' objects are IMMUTABLE - once we create them, we
# CANNOT mutate (modify) them.
