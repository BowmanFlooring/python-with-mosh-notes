# XARGS

def multiply(x, y):
    return x * y


multiply(2, 3)

# This is fine. 2 parameters, 2 arguments
# But say we want to do this:


def multiply(x, y):
    return x * y


multiply(2, 3, 4, 5)

# This would NOT work! Too many arguments!
# This can be fixed...


def multiply(*numbers):
    # We use a plural name to indicate, this is a 'collection of arguments'.
    print(numbers)


multiply(2, 3, 4, 5)

# RESULT
# (2, 3, 4, 5)
# Why no multiplication?!?!

# Our numbers, encapsulated in parentheses, are in a 'Tuple'.
# Tuples are kind of like lists (they ARE iterable!), but they cannot
# be modified in any way.

# A 'list' vs. a 'tuple' would look like:
"""
LIST:    [2, 3, 4, 5]
TUPLE:   (2, 3, 4, 5)
"""
# The ONLY difference is the NOTATION - the parentheses/brackets.

# With a Tuple, we could do this:


def multiply(*numbers):
    for number in numbers:
        print(number)


multiply(2, 3, 4, 5)

# RESULT
# 2
# 3
# 4
# 5

# So, we 'iterate' over this tuple, and for each iteration,
# we get one number, printed on the terminal.

# Now, with one simple change, we can calculate the product
# of all these numbers:


def multiply(*numbers):
    # Let's define a variable, initially we'll set it to 1.
    total = 1
    for number in numbers:
        # Then, for each iteration, multiply 'total'
        # by the current number.
        # total = total * number
        # OR we could use an 'augmented operator'!
        total *= number
    return total

# Now, with this implementation, we cant print
# the result to the terminal.


print(multiply(2, 3, 4, 5))

# RESULT
# 120

# It now has successfully multiplied together all the numbers
# within a Tuple!
