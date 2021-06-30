#-------------------------------------------------------------------------------
# Tuples

# We've discussed Tuples quite a few times in this course. Now, let's take a
# closer look at them.

# A 'Tuple' is basically a 'READ-ONLY' list. We can use it to CONTAIN a sequence
# of objects, but we CANNOT MODIFY this sequence. We can't add a new object; we
# can't remove, or otherwise modify, an existing object.

# Let's build our tuple. In python we use parentheses to define a tuple. But, as
# a side note, if we exclude parentheses, Python will still recognize the set of
# items as a tuple. Let's test out that process first - we can do that by first
# encapsulating our variable with 'type'; then print the result to the terminal:
point = 1, 2
print(type(point))
"""
RESULT:
<class 'tuple'>
""" 

# It's worth mentioning, that if you try that with only one item, Python thinks
# you're defining an 'integer'. Fair enough, Python. Nice play. Let's try it:
point = 1
print(type(point))
"""
RESULT:
<class 'int'>
"""
# So, to make a single item a tuple, add a trailing comma. Let's try that now:
point = 1,
print(type(point))
"""
RESULT:
<class 'tuple'>
""" 
# And if you want do define an empty tuple, you do that with empty parentheses:
point = ()
print(type(point))
"""
RESULT:
<class 'tuple'>
""" 

# Now, similar to lists, we can 'concatenate' two tuples. This is very easy:
point = (1, 2) + (3, 4)
print(point)
"""
RESULT:
(1, 2, 3, 4)
"""

# Also, we can use the multiplication operator to repeat a tuple:
point = (1, 2) * 3
print(point)
"""
RESULT:
(1, 2, 1, 2, 1, 2)
"""

# Along with all those ways to create a tuple, we can convert a list to a tuple.
# To perform that operation, we use the 'tuple' function. The parameter that
# Python sets for the 'tuple' function is simply - an iterable. So we can pass
# ANY iterable as an argument, and it will return a tuple. Here are a couple 
# examples of that in action:
point = tuple([1, 2])
print(point)
"""
RESULT:
(1, 2)
"""
point = tuple("Hello, Dakota")
print(point)
"""
RESULT:
('H', 'e', 'l', 'l', 'o', ',', ' ', 'D', 'a', 'k', 'o', 't', 'a')
"""

# Now, let's use a bit of a bigger tuple for these next examples:
point = (1, 2, 3, 4, 5, 6)
# We can find the index of an item, or a range of items:
print(point[0])
print(point[0:4])
# We can unpack 
a, b, c, d, e, f = point
# And similar to lists, we can check for the existence of an item in the tuple:
if 10 in point:
    # And print a message if if does exist:
    print("exists")

# As a reminder, tuples are 'immutable' - they cannot be modified. So, it may
# seem hard to imagine a real-world use-case. Well, let's say you're using some
# list, and the contents are sensitive. At least, their existense and also their
# place in the list is of high importance. You can convert the list to a tuple,
# that way you don't accidentally add, remove, or modify any of the items.
