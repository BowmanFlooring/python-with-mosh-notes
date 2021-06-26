# Lambda Functions

# The term 'lambda expression', or 'lambda function', is
# used in other programming languages as well. Basically,
# it's a simple, one line anonymous function that we
# can pass into other functions.

# To continue from the last lecture, 'sorting lists', let's
# look at our previous code:

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)

# This code can be made cleaner with a lambda expression,
# or an anonymous function, so we don't have to define this
# function first {line 18}, and then pass it {line 22}.


def sort_item(item):
    return item[1]


# The syntax for lambda is 'parameters:expression'
# Our parameter (we only have one) is 'item';
# Our expression is 'item[1]'

items.sort(key=lambda item: item[1])
print(items)

# So the two lines we wrote to define our function
# are no longer necessary.
#  * See: {line 18, 19} or {line 30, 31} *

"""
RESULT:
[('Product2', 9),
('Product1', 10),
('Product3', 12)]
"""

# Simpler Code, Same Result.
