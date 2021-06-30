# List Comprehensions

"""
In the past two lectures, we have learned how to write and use
the 'map' and 'filter' functions. In Python, we also have what's
called 'list comprehension', and it has a much cleaner-looking
syntax. Here's what it looks like, compared against the 'map'
and 'filter' functions.
"""
# Our listed items:
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

# The 'map' function:
prices = list(map(lambda item: item[1], items))
# 'list comprehension':
prices = [item[1] for item in items]

# lines 18 and 20 are EXACTLY the same. Line 20 is much
# easier to read. But that doesn't mean we won't stumble
# across a use case by an overly-optimistic developer
# some time down the road...

# The 'filter' function:
filtered = list(filter(lambda item: item[1] >= 10, items))
# 'list comprehension':
filtered = [item for item in items if item[1] >= 10]
