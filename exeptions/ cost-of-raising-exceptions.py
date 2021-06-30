# Cost of Raising Exceptions

# Let's run a test to test out this theory. For this, we need to import
# the 'timeit' function from the 'timeit' module.
from timeit import timeit

# to use 'timeit', we need to define a variable, and define it with our code,
# like this:
code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
"""
# Then, we use the 'timeit' function, and pass in two arguments. The first is
# our variable. The second is a keyword argument, which is where we will 
# specify the number of times we want our code excecuted. We want this number 
# to be high - we want to be able to see the cost of raising exceptions. We 
# then print the result.
print("first code =", timeit(code1, number=10000))

# To make this cleaner - a.k.a, to prevent 10,001 lines of text printed on the
# terminal, replace the 'print' statement in the 'try' block of our code with
# the 'pass' statement. An 'except' clause can't be empty, so the 'pass'
# statement is basically just a filler: 
from timeit import timeit

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""
print("second code =", timeit(code2, number=10000))
'''
RESULT:
first code = 0.003558457000000001
'''

# Let's try a different approach. Let's 'return None' instead of raising an
# exception in our function. Remember, 'None' represents the absense of a value.
# This eliminates the need for the 'try' block. We can then store
# 'calculate_xfactor(-1)' in a variable, and compare it with None:
from timeit import timeit

code3 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age



xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""
print("third code =", timeit(code3, number=10000))
# Now, let's compare the speed of 'code2' vs. 'code3':
'''
RESULT:
third code = 0.001556175
'''

# Quite a bit faster!
