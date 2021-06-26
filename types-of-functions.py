# Types of Functions

# There are TWO types of functions in Python.

# 1. functions that peform tasks
#           e.g. print()

# 2. functions that calculate and return a value.
#           e.g. round(2.3)

# EXAMPLE 1


def get_greeting(name):
    print(f"Hi {name}")

# EXAMPLE 2


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Dakota")

# In the first example, we are locked into printing
# something in the terminal. In the future, if we want to write
# that message in a file, or in an email, we would have to create
# another function. So, we could NOT re-use the 'greet' function
# from example 1 in other scenarios.

# In contrast, the second form isn't tied to printing at terminal.
# We could, for a simple example:

# Write that message to a file, like:

file = open("content.txt", "w")
file.write(message)

# we will learn more about those 2 lines above at a later date.
# the takeaway here is that we have this variable, 'message', and
# we can do whatever we want with it. It's not confined to just
# simply printing in the terminal because we are 'returning' the value!

# BONUS:
# now, what if we try and call the func. w/ 'print'?


def greet(name):
    print(f"Hi {name}")


print(greet("Dakota"))

# RESULT
# Hi Dakota
# None
# ALL FUNCTIONS RETURN 'None' BY DEFAULT, UNLESS WE
# SPECIFY A RETURN, like:


def greet(name):
    print(f"Hi {name}")
    return "..."


print(greet("Dakota"))
