#-------------------------------------------------------------------------------

# Dictionary Comprehension

# Here's a bit of code that can be condensed and rewritten down into one line:
# Step1: 
#   Define a list (empty)
# Step2: 
#   Iterate over te string object
# Step3: 
#   For each iteration, we get 'x', multiply it by two, and then add to list.

values = []
for x in range(5):
    values.append(x * 2)

#
# In a previous lecture, we talked about this exact code structure. Whenever
# we see this code pattern - or we write it ourselves - we can simplify it. So,
# the 'map' function works, but preferrably - 'list comprehension'.
# Check out the proper syntax for 'LIST COMPREHENSION':

#                   [expression for item in items]

# So, what we're doing is this:
# We iterate over an iterable. 
# In each iteration, we get 'item'.
# Then, we do something with it ('expression').
# 
# In our example....
# Our 'iterable' is the 'range' object - (range(5)), specifically.
# Our 'item' is 'x'.
# The expression we're using is 'x * 2'.
# We should also store the whole snippet in a variable.

# So, all together now:
values = [x * 2 for x in range(5)]

# This code is EXACTLY THE SAME as the code on {line 13-15}.
# Two less lines of code, and the syntax looks better.

# This is NOT exclusive to lists! We can also use this with sets
# and dictionaries. We know that a set is enclosed wit curly braces. So, all
# we need to do is replaces the square brackets with curly's.
values = {x * 2 for x in range(5)}
# Let's print it:
print(values)
'''
RESULT:
{0, 2, 4, 6, 8}
'''

# But, how would we do this with a dictionary? They both use curly braces. But,
# for the syntactical difference; in sets, we just have values. In a 
# dictionary, we have values mapped to keys; the pair separated with a colon.
# SET:  {1, 2, 4, 6}
# DICT: {1: "x", 2: "y"}
# So, to change our 'list comprehension' expression in order to produce a 
# dictionary, we simply change: 
# 'x * 2'  -->  'x: x * 2' 
values = {x: x * 2 for x in range(5)}

# So, instead of defining a variable with an empty set, looping over an iterable,
# and then, with each iteration, adding something to that dictionary....
# We can do all of that much easier if we use 'dictionary comprehension'.

# NOTE: This COMPREHENSION concept can be used with:
# Dictionaries
# Lists
# Sets
# Tuples  <-|  To Be Continued...
