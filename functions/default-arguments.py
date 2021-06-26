# Default Arguments

# If we want to make a certain parameter optional, that's easy.

# Example:
def increment(number, by=1):
    return number + by


print(increment(2))

# Instead of supplying our two parameters like normal, we have
# SUFFIXED the 'by' parameter.
# By doing this, a second argument no longer is required.
# If the 2nd argument isn't provided, then it defaults to our
# chosen value.
# If a 2nd argument IS provided, then that value is used.
# Pretty simple concept!

"""
*** just remember!!! ***
if you're adding one of these 'default' arguments
as a parameter, it MUST be the LAST parameter! 
You CANNOT add another standard parameter after.

In SUMMARY:
OPTIONAL PARAMETERS GO AT THE END.
"""
