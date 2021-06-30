#-------------------------------------------------------------------------------

# Handling Exeptions

# Looking at the code from 'Exeptions':
# age = int(input("Age: "))

# To handle a possible exeption on this code, we need to put it in 
# a 'try' block. Here's what that looks like:
try:
    age = int(input("Age: "))
except ValueError as ex:
    print("You didn't enter a valid age.")
    print(ex)
    print(type(ex))
else:
    print("No exceptions were thrown.")
print("Execution continues.")

# On {line 12, 13}, that's basically saying 'if a ValueError exception
# occurs, print this statement".

# on {line 17}, the 'else' statement will only be executed if NO EXCEPTIONS
# are thrown!

# As far as these 3 items below:
# 'as ex:' on {line 12}
# print(ex)
# print(type(ex))

# These are just an added optional little snippet you could add to make
# your exceptions seem more interactive or responsive. They are 100% NOT
# required for it to work.