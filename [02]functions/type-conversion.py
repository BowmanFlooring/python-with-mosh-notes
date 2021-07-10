# -------------------------------------------------------------------------------

# Type Conversion - and the 'input' function

# we use the 'input' fuction to get input from the user:

x = input("x: ")
y = x + 1

# if we run this as is, python will try to execute "1" + 1.
# we cannot add a two different objects together, so we need to
# do a 'type conversion'. Types can be converted very easily, with
# int(x) , float(x) , bool(x) , str(x)
# and to check the 'type' of an object, use the 'type' function:

type(x)

# and pass the object (in this case, x) as an argument.
# make sure to encapsulate the fuction with 'print' to see results!
# Here's what the entire thing would look like now:

x = input("x: ")
print(type(x))

# since we need to convert the input to a string....

x = input("x: ")
y = int(x) + 1
print(f"x: {x}, y: {y}")

# now python can successfully add x and y together, as integers!

# in python, there's the concept of trucy and falsy
# Falsy: "", 0, None
# Trucy: Everything Else!

# QUIZ QUESTION: What are the 3 Primitive Types in Python:
# STRINGS, NUMBERS, BOOLEANS
