#------------------------------------------------------------------------------

# Raising Exceptions

# NOTE: Raising exceptions is costly! This is only part of the course to
# demonstrate what this looks like. It is not advised:

def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
