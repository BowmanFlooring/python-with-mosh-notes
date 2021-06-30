# Map Function

# This lecture will be expanding on the use of the 'lambda' function.

# Say we have a list of items, and we want to transform the list
# into a list of numbers (in this case, a list of prices)

# Here's the list (we will continue this ex. with this familiar list):
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

# Now, let's define a variable, and set it to an empty list:
prices = []
# Then iterate over that list of items
for item in items:
    # Then return the price of each item
    prices.append(item[1])

# Now, let's print the prices:
print(prices)

"""
RESULT:
[10, 9, 12]       
"""
# It gives us this list of items.
# With this code, we have transformed the original list {lines 9-13}
# into a new list.
# And, OF COURSE, there's a better way to do it!

# For this we will use the 'map' function.
# The 'map' function takes two parameters:
# 1. func <-- Here, we can pass in a lambda function!
# 2. *iterables (one or more iterables) <-- Here, we'll use our list

map(lambda item: item[1], items)

# Let's store this in a variable, called 'x':
x = map(lambda item: item[1], items)
# Then, print the variable:
print(x)

"""
RESULT:
<map object at 0x108c4f3c8>
"""
# This function returns a map object, which itself is actually iterable.
# So, we can easily iterate over it:
x = map(lambda item: item[1], items)
for item in x:
    print(item)

"""
RESULT:
10
9
12
"""
# Alternatively, we can convert this map object into a list object.
x = list(map(lambda item: item[1], items))

# Remember, we can pass ANY iterable to the list function to
# create a new list. Our 'map' object is iterable, so it works here.

# Then, change the variable 'x' to 'prices':
prices = list(map(lambda item: item[1], items))
# And simply print 'prices':
print(prices)

# This eliminates the need for our 'for' loop as well {line 53}.
"""
RESULT:
[10, 9, 12]
"""

# So, in summary, the 'map' object takes a lambda function, and applies
# it to every item in the iterable.
