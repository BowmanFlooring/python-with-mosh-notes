def increment(number, by):
    return number + by


result = increment(2, 1)
print(result)

# RESULT: 3

# we can simplify this code by getting rid of the 'result'
# variable, like:

print(increment(2, 1))

# This prints the exact same thing to the terminal.
# RESULT: 3

# Here's Why:
# Python first executes 'increment(2, 1)', which it then stores
# the result in a variable that we don't ever see. Then, python
# passes that variable as an ARGUMENT to the 'print' function!

# If another Dev is reading this code, it may not be exactly clear
# as to what we are saying in our 'print' function.
# To make it more readable, we can PREFIX our ARUMENTS with the
# name of the parameter, like:

print(increment(2, by=1))

# This now almost reads like plain english!
# "Increment 2 by 1"
# In this example, 'by=1' is a 'keyword argument'
