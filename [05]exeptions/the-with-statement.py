# -------------------------------------------------------------------------------

# The With Statement

# The 'with' statement is used to automatically release external resources. so,
# it eliminates the need for the 'finally' clause. Let's go back and look at
# our code for the last lecture, but this time we will use the 'with' statement:
try:
    with open("handling-different-exceptions.py") as file:
        print("File Opened.")
    age = int(input("Age: "))
    xfactor = 10 / age  # <- here's the new line
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")

# Also, to open a second file (maybe you want to write to it), just add a comma
# after 'file' in the first line of the with statement, adding the same code
# as what is on the left side of the comma - of course, choosing a different
# file name is implied.
