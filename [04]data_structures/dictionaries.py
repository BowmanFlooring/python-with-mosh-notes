# -------------------------------------------------------------------------------
# Dictionaries

# This type of data structure is basically a collection of 'key:value' pairs.
# We would use a dictionary in Python to map a key to a value. A real-world
# example of this - a phone book.

# For the key, the object MUST BE IMMUTABLE. But, for the value, it can be any
# type of object. There are no limitations.

# Here's one way to define and create a dictionary:
point = {"x": 1, "y": 2}

# Also, we can use the 'dict' function. So, just like these familiar functions
# we have available:
# list()
# tuple()
# set()
# We can now add 'dict()' to the list.

# When calling this function, we can pass in one or more keyword arguments. So,
# let's redefine our 'point' variable:
point = dict(x=1, y=2)
# It's esentially the same thing, but with much cleaner syntax.
# ----
# Now that we have a dictionary, here's a couple things we can do with it:

# Get the value associated with a key, using it's index.
point["x"]
print(point["x"])
# NOTE: We cannot access the index of an item with an integer, as we do with
#        lists. We use that acual key, and it will give us that key's value.

# Change the value of a key:
point["x"] = 10
# This will change the value of 'x' from '1' to '10'.

# We can add a new key to the dictionary:
point["z"] = 20

# NOTE: If we try to find the index of an item that is NOT in the list,
# Python will give us back an Error. There are two ways to fix that. One
# workaround would be to add an if statement. The other, use 'get' method.

# Ex.1 (if statement)
if "a" in point:
    print(point["a"])

# Ex.2: (get method)
point.get("b")
print(point.get("b"))
# NOTE: By default, this would now return 'None' if 'b' is non-existent. We
# can pass a second argument, and that would replace 'None':
point.get("b")
print(point.get("b", 0))

# Also, we can delete an item by using the 'del' statement:
del point["x"]
print(point)

# And finally, we can loop (iterate) over a dictionary:
for key in point:
    print(key, point[key])
# OR
for x in point.items():
    print(x)
'''
RESULT:
('y', 2)
('z', 20)
'''
# For each iteration, we get a tuple. In each tuple, we get the key and it's
# value. So, we can unpack it in place of 'x':
for key, value in point.items():
    print(key, value)
'''
RESULT
x 2
y 20
'''
