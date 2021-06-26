# Adding Or Removing Items

# Add

# For adding items to a list, we have 2 options, depending
# on where we want to add the item.
# If we are adding an item to THE END of the list,
# we should use the 'append' method.
# ------------------------------------------------------
#
#                *** REMEMBER THIS ***
#           When a function is part of an object
#  (like the function 'append' is to the object 'letters')
#               we refer to that function
#                       as a
#                     'method'.

letters = ["a", "b", "c"]
letters.append("d")
print(letters)
"""
RESULT:
['a', 'b', 'c', 'd']
"""

# For adding items to a certain position, we should use
# the 'insert' method.

letters = ["a", "b", "c"]
letters.insert(0, "-")
# This says " at index '0', add '-' "
print(letters)
"""
RESULT:
['-'. 'a', 'b', 'c', 'd']
"""

# For removing objects at end of list, we should use
# the 'pop' method.

letters = ["a", "b", "c"]
letters.pop()
print(letters)
"""
RESULT:
['-', 'a', 'b', 'c',]
"""

# If we want to remove an item, and we don't know it's
# specific index, we should use the 'remove' method.

letters = ["a", "b", "c"]
letters.remove("b")
print(letters)
"""
RESULT:
['a', 'c', 'd']
"""

# *** *** *** *** *** ***
# This tells python to remove the FIRST occurrence of 'b'.
# If we want to remove ALL "b's" from the list, we would have
# to loop over this list, and remove each 'b' individually.
#   *** it's quicker than you think! Python is fast 👽 ***

# we have another method for removing items from a list,
# and that is by using the 'del' statement.
#                 ***'del' = 'delete' ***

# Ex. 1 - deleting ONE item
letters = ["a", "b", "c"]
del letters[0]
print(letters)
# Ex. 2 - deleting a RANGE of items
letters = ["a", "b", "c"]
del letters[0:3]
print(letters)

# This is what separates the 'pop' method and the 'del'
# statement. 'pop' can only remove a single item, whereas
# the 'del' statement can remove either
# A. a single item, or
# B. a range of items.

# And finally, to remove ALL objects/items from the list,
# we should use the 'clear' method.
letters = ["a", "b", "c"]
letters.clear()
print(letters)
"""
RESULT:
[]      <-- 'empty list' 
"""
