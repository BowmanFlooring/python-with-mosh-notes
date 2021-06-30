#°°°°°°°°°#°°°°°°°°°#°°°°°°°°°#°°°°°°°°°#°°°°°°°°°#°°°°°°°°°#°°°°°°°°°#°°°°°°°°°
#                                                                           ‹80›
# Arrays

# We've learned about all types of lists. Another one of those is an 'array'. An
# array is much more efficient - usually, the performance difference isn't all
# that noticeable unless we're working with >= 10,000 items. So, if our Python
# program is causing performance issues in any way, we should check our code to
# see if we can replace our list with an array.
# *IF YOU DON'T HAVE ANY PERFORMANCE ISSUES, THEN NO NEED TO REINVENT THE WHEEL*

# To use arrays, we need to import the 'array' class from the 'array' module:
from array import array
# The first parameter listed for 'array' is 'typecode'. Typecode is a type of
# string that determine the type of objects in your array. Here's some content
# from the first result in a 'python3 typecode' google search:
'''
TYPE CODE ------ C TYPE ------ PYTHON TYPE ------ MIN. SIZE(bytes) ------ NOTES
'b' ......... signed char ........ int ............... 1 ......................
'B' ....... unsigned char ........ int ............... 1 ......................
'u' ............ wchar_t ... Unicode character ....... 2 ................. (1).
'h' ........ signed short ........ int ............... 2 ......................
'H' ...... unsigned short ........ int ............... 2 ......................
'i' .......... signed int ........ int ............... 2 ......................
'I' ........ unsigned int ........ int ............... 2 ......................
'l' ......... signed long ........ int ............... 4 ......................
'L' ....... unsigned long ........ int ............... 4 ......................
'q' ....... signed long long ..... int ............... 8 ......................
'Q' ..... unsigned long long ..... int ............... 8 ......................
'f' ............. float .......... int ............... 4 ......................
'd' ............ double .......... int ............... 8 ......................
'''
# For signed integers, we should use the lowercase 'i'. Then we will add a few
# objects to the array, and assign the array to a variable:
numbers = array("i", [1, 2, 3])

# In this object, we have methods, similar to the 'list' method, for adding an
# item(s), removing item(s), etc.:

# To add to the end:
numbers.append()
# To add at a specific index:
numbers.insert()
# Remove the last item:
numbers.pop()
# Remove an item at a given index:
numbers.remove()
# Access items by their index:
numbers[0]

# Unlike lists, every object in arrays are 'typed' - a specific type
# must be defined. We defined ours with the 'signed' int type. So,
# if we try to add a floating point number - or ANY other kind of 
# object for that matter - to this array, we will get an error.
# Let's test this out by trying to add a floating point number:
numbers = array("i", [1, 2, 3])
numbers[0] = 1.0
'''
RESULT:
TypeError: integer argument expected, got float
'''

# REMEMBER: an array's type is defined as a single-letter string
# object, passed in the function's first argument.
