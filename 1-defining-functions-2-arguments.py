# Defining Functions

def greet():
    print("Hi there")
    print("Welcome Aboard")


greet()

# Arguments

# in between the '()' when defining our functions, we can put
# our required parameters for the function, like:

# NOTE: by default, the parameters we define in our functions will
# be REQUIRED in order for python to correctly execute it!!!


def greet(first_name, last_name):
    print(f"Hi there, {first_name} {last_name}!")
    print("Welcome Aboard")

# The two names we are going to pass are called 'Arguments'.


greet("Dakota", "Bowman")

# RESULT
# Hi there, Dakota Bowman!
# Welcome Aboard

# LOTS OF DEVS STILL DON'T KNOW THE DIFF. BETWEEN
# 'ARGUMENTS' and 'PARAMETERS'!!!!

# Parameter: the INPUT we define for our functions.
# Arguments: the ACTUAL VALUE for a given parameter.
