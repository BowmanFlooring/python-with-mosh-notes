# Sorting Lists

# Firstly, we have an unsorted list, and we want it sorted:

numbers = [3, 51, 2, 8, 6]
numbers.sort()
print(numbers)

"""
RESULT:
[2, 3, 6, 8, 51]
"""
# What if we want to sort this list in DECENDING order?

numbers = [3, 51, 2, 8, 6]
numbers.sort(reverse=True)
print(numbers)

"""
RESULT:
[51, 8, 6, 3, 2]
"""
# In addition to the 'sort' method, Python also has a builin
# function called 'sorted'.
# The 'sorted' function take 3 parameters:
#   an 'iterable', a 'key', and 'reverse'
# Also - unlike 'sort', the sorted function will NOT modify
# the original list. It only returns a new sorted list.
# We can check that by running them in succession:

numbers = [3, 51, 2, 8, 6]
print(sorted(numbers))
print(numbers)

"""
RESULT:
[2, 3, 6, 8, 51]
[3, 51, 2, 8, 6]
"""

# Here's the 'sorted' function again, but with a 2nd argument:
print(sorted(numbers, reverse=True))

# Now, what if we want to sort a list of complex objects?
# For example, let's say we have list of Tuples. Let's imagine we # have to build an application for processing orders. We have in
# front of us, a list of order items. Every item is a Tuple.
#     1. The Product NAME, 2. The Product PRICE

items = [
    ("Product1", 10)
    ("Product2", 9)
    ("Product3", 12)
]

# If we try to sort this list right now, as is, Python will
# NOT know how to sort it. It will be returned back EXACTLY
# the same.
# For situations like this, we need to
# DEFINE A *FUNCTION* THAT PYTHON CAN USE FOR SORTING LISTS!!
# *** this is where 'custom functions' come in to play ***


def sort_item(item):
    # * since each item is a tuple, we can get the *price*
    # * of each item by using '[]'; so we'll
    # * "return item of 1"
    return item[1]


# so all this function does is take an item, a tuple, and
# return it's price.
# now, python is dealing with a list of numbers, and
# of course it knows how to sort that!
#
# finally,  we  need  to  pass  the  function  we  just  made
# when sorting our list of items. so once again, lets take a
# look at the 'sort' method:
#
items.sort()
#
# Here's the official description of the 'sort' method:
"""
    (*, key: None = ..., reverse: bool = ...) -> None
    Sort the list in ascending order and return None.

    The sort is in-place (i.e. the list itself is modified) and table (i.e. the order of two equal elements is maintained).

    If a key function is given, apply it once to each list item and  sort them, ascending or descending, according to their function  values.
   
    The reverse flag can be set to sort in descending order.
"""
# The first parameter required by the 'sort' method is 'key'.
# So, let's try to pass our function as an argument:

items.sort(sort_item)

# Note that we are NOT CALLING this function;
# We're simply passing a reference to this function.

# When Python attempts to sort this list of items, it gets
# each item, and then passes each item to our sort function.

# Then, of course, end it with a print statement:

print(items)

# So, everything together looks like this:

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]


def sort_item(item):
    return item[1]


items.sort(sort_item)
print(items)

"""
RESULT:
TypeError: sort() takes no positional arguments
"""
# To fix this, we need to specify that our function,
# 'sort_item', is a key. We do this like:

items.sort(key=sort_item)
print(items)

"""
RESULT:
[('Product2, 9),
('Product1', 10),
('Product3', 12)]
"""
# This gets our list sorted by item! BUT! But, but, but...
# There's always a better/prittier way to write your code!

# ..................TO BE CONTINUED.......................
