# Finding Items

# Let's say we want to find the index of letter 'a'.
letters = ["a", "b", "c"]
print(letters.index("a"))
"""
RESULT:
0  <-- the index of 'a'
"""

# Let's say we try to find the index of an
# object that does NOT exist:
letters = ["a", "b", "c"]
print(letters.index("d"))
"""
RESULT:
ValueError: 'd' is not in list
"""

# AS A SIDE NOTE:
"""
In other programming languages, specifically C based 
languages, attempting to find the index of an item that
isn't in the list will return '-1'. But in Python, we
get '0'
  *** Remember, in Python, we have 'Trucy' and 'Falcy'.
        '0' is a 'Falcy' statement/expression.
"""

# To prevent this from happening, we need to first check
# to see if 'd' exists, THEN find it's index - that is,
# if it does in fact exist.
letters = ["a", "b", "c"]
if "d" in letters:
    # This reads 'if "d" is in letters'
    print(letters.index("d"))
message = 23

# Here's the 'count' method, which returns the number of
# occurrences the given item shows up in the list.
letters = ["a", "b", "c"]
letters.count("d")
if "d" in letters:
    print(letters.index("d"))
