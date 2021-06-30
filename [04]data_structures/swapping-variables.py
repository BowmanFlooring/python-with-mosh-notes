# Swapping Variables

# Let's say we have two variable, 'x' and 'y', and we want to swap their values.
x = 10
y = 20
# To do this, we can define a third variable, 'z':
z = x
# Now, the value of 'x' has been 'backed up' to another variable. This will now
# allow us to overwrite 'x' with the value stored within the variable 'y', and
# then finally overwrite 'y' with 'z' - which is a copy of the original 'x':
x = y
y = z
# Let's check to be sure:
print("x", x)
print("y", y)
"""
RESULT:
x 20
y 10
"""

# Nice! But, in Python, there's always a better way! We don't need a third
# variable to for backup, and it only takes one line of code:
x, y = y, x
"""
RESULT:
x 20
y 10
"""
# Too easy. To explain what going on, we are esentially unpacking the right side
# of the expression into the left side. Here's why:
# Remember, Python recognizes two items separated by a comma as a tuple. So, the
# right side is us defining a tuple. On the left side, we are naming two
# variables. In Python, we can name multiple variables on one line.
