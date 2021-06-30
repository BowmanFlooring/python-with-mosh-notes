# Filter Function

# Let's say we want to get items out of our  list:.

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

# but we only want items from the list that  cost >= $10
# -----
# For this, we should use the 'filter' function.
# 'filter' takes 2 parameters:
# 1. a function (or None), and
# 2. an iterable

# Return an iterator yielding those items of iterable for which
# function(item) is true. If function is None, return the items
# that are true.

# Basically, it will apply a function to each item in an iterable,
# and if it matches some criteria, it will return the item.

# We are starting to see a pattern within these builtin
# Python functions........

# So, for this example:
filter(lambda item: item[1] >= 10)

# Here, each list item (lambda item:) will be checked against
# the part of the expression after the colon, which is just
# a statement that is really either true or false.
# If true, return the item!

# Now, lets pass our 2nd argument, 'items', and then
# we can store the entire thing in a variable we'll call 'x'.
x = filter(lambda item: item[1] >= 10)
print(x)

"""
RESULT:
<filter object at 0x105bc23c8>
"""

# This filter object, just like the map object from last lecture,
# is iterable! Because of this, we can loop over it, and we can
# also convert it to a list right away:
filtered = list(filter(lambda item: item[1] >= 10))
print(filtered)

"""
RESULT:
[('Product1', 10),
('Product3', 12)]
"""

# So, as you can see, we only get back the products that
# cost either $10 or over.
