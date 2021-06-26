# Filename = 'mosh-1.py'
# Python Programming w/ Mosh
# --------------------------
# Variables

# variable names should be clear and descriptive!
# all letters in variables should remain lower case
# in variables with multiple names, use underscore
# always put space between the "="

students_count = 1000  # integer
rating = 4.88  # floating point num.
is_published = False  # boolean (True/False)
course_name = "Python Programming"  # string (a 'string' of chars.)
print(students_count)  # <-- the print = 1000
# --------------------------
# Strings

# use double quotes to enclose strings, like:
course = "Python Programming"

# single quotes can be used, but double quotes preferred

# use triple quotes for strings spanning multiple lines, like:
course_description = """
Hello, and welcome to the course!
I'm your instructor, Mosh.
This course will teach you all you
need to know about Python. Hopefully
by the end, you'll be 100% satisfied!
"""
# --------------------------
# Functions (a reusable piece of code to perform a specific task)

# Python has built-in, reusable, functions
# Ex:
course = "Python Programming"
len(course)  # **
# ** the 'len' func. outputs the num. of chars. in 'course'
# our var., 'course', is given to the func. as an *argument*
# some fuctions require arguments (inputs of the function)

# if you want to index a certain character, or range of
# characters within a string, use '[]', like:
print(course[3])
print(course[-1])
print(course[0:4])
print(course[:4])
print(course[0:])
print(course[:])
# --------------------------
# Escape Sequences

# \", \', \\, \n (new line),
# the backslash is the escape *character*, and when used before a
# character (chars. listed above) that usually performs a simple
# function, it enables the use of the actual char. instead.
#   - the exception is '\n' <-- this means "new line"
course = "Python \"Programming"
print(course)  # <-- the print = Python "Programming
# --------------------------
# Formatted Strings

# Ex.1:
first = "Dakota"
last = "Bowman"
full = first + " " + last  # <-- this is called 'concatenation'
print(full)  # <-- the print = Dakota Bowman

# Ex.2:
first = "Dakota"
last = "Bowman"
full = f"{first} {last}"
print(full)  # <-- again, the print = Dakota Bowman
# this is a "formatted string"
# This example keeps simple OR complex code much cleaner-looking.
#   *at runtime, python just replaces everything in curly braces,
#   & the space remains a space. so, we could put any expression
#   within those curly braces and receive it's value
# --------------------------
