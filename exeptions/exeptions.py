# -------------------------------------------------------------------------------

# Exeptions

# An exeption is a kind of error that terminates the execution of a program.
# Here's an example of a basic error. If we run this code:
numbers = [1, 2]
print(numbers[3])
'''
RESULT:
Traceback (most recent call last):
File "*/*/*/*/*/*/handling_exeptions.py",
line 8, in <module>
print(numbers[3])
IndexError: list index out of range
'''
# This is called 'Throwing An Exeption'

# Here's a little bit of a different example. In this example, we want to
# receive input from the user, in the form of an integer:
age = int(input("Age: "))
# So, if the user enters a non-numeric value:
'''
RESULT:
Traceback (most recent call last):
File "*/*/*/*/*/*/handling_exeptions.py",
line 17, in <module>
age = int(input("Age: "))
ValueError: invalid literal for int()with base 10: 'a'
'''

# It's our job as a programmer to handle these exeptions!
# That will be saved for the next lecture....