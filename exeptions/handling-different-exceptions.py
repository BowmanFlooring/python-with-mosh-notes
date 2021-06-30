# -------------------------------------------------------------------------------

# Handling Different Exceptions
# Let's look at the code from the last lecture, but with an added line:
try:
    age = int(input("Age: "))
    xfactor = 10 / age  # <- here's the new line
except ValueError as ex:
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
print("Execution continues.")

# So, what if someone accidentally types '0'?
# Here's what that error looks like:
'''
RESULT:
Traceback (most recent call last):
File "*/*/*/*/*/*/handling-different-exceptions.py",
line 3, in <module>
xfactor = 10 / age
ZeroDivisionError: division by zero
'''
# So, as our code is written right now, we aren't handling 'ZeroDivisionError'
# exceptions - only "ValueError" exceptions. Let's add another 'except'
# clause:
try:
    age = int(input("Age: "))
    xfactor = 10 / age
except ValueError:
    print("You didn't enter a valid age.")
except ZeroDivisionError:
    print("Age cannot be zero.")
else:
    print("No exceptions were thrown.")
print("Execution continues.")

# when we have 2 except clauses, and we want to show the user the same error
# on either exception, the code can be combined:
try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
print("Execution continues.")
