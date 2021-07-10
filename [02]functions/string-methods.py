# String Methods
# EVERYTHING IN PYTHON IS AN OBJECT,
# AND OBJECTS HAVE FUNCTIONS WE CALL METHODS,
# AND WE ACCESS THOSE METHODS WITH 'DOT' NOTATION.

import math

course = "python programming"

print(course.upper())    # <--  PYTHON PROGRAMMING
print(course.lower())    # <--  python programming
print(course.title())    # <--  Python Programming
print(course.strip())    # <-python programming(no whitespace before OR after)
print(course.rstrip())   # <--  python programming(no whitespace after)
print(course.lstrip())   # <--python programming (no whitespace before)

# notice, it's always some_variable.some_method !!!!
# Here's a couple more examples...

print(course.find("Pro"))  # <-- 7 (the index [position of 1st letter] is 7)
print(course.replace("p", "j"))  # <-- jython jrogramming
print("pro" in course)  # <-- True (boolean)
print("swift" in course)  # <-- False (boolean)