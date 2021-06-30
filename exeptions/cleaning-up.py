#-------------------------------------------------------------------------------

# Cleaning Up

# There will be times when we have to work with externat resources within our
# code. It is good practice to release those resources when we are done with
# them. That way, no other programs have troubles if they also need to
# use whatever we have just used. For example, opening/closing a file:

# We can open files with the 'open' function, which returns a file object:
try:
    file = open("handling-different-exceptions.py")
    age = int(input("Age: "))
    xfactor = 10 / age  # <- here's the new line
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
# At the end, we should add a 'finally' clause to close the file:
finally:
    file.close()

# The finally clause is where we release any external resource we've used.

