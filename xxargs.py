# XXARGS

"""
In the previous lecture, we saw that we have a 
synax to pass a variable number of arguments
to a function [an asterisk - (*numbers)].

We have a variation of that syntax, which is
TWO asterisks.
"""

# Let's imagine we're gonna use this function to save
# information about a user:


def save_user(**user):
    print(user)


# Here we can add multiple keyword arguments, like:

save_user(id=1, name="John", age=22)

# RESULT
# {'id': 1, 'name': 'John', 'age': 22}

# Look at the syntax here. Let's break it down:
"""
Firstly, we have the curly braces.
Inside the curly braces, we have multiple 'key: value' pairs.
This object as a whole that we see here, 
it's called a 'dictionary'.

A 'Dictionary' is another complex type, or data structure, in Python.
We will talk about these more in depth later in the course.
"""
# What we should take away from this example is this:
# When using double asterisks in Python, we can pass in
# multiple 'key: value' pairs, or 'keyword arguments', and Python
# will automatically package them into a Dictionary.
# So, the "**user" object we use here is a dictionary,
# and notice that the bracket notation can get the value of
# various keys in this dictionary. For example:


def save_user(**user):
    print(user["id"])


save_user(id=1, name="John", age=22)

# RESULT
# 1


def save_user(**user):
    print(user["name"])

# This would print:
# John


def save_user(**user):
    print(user["age"])

# This would print:
# 22
