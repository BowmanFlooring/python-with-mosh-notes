# Zip Function

list1 = [1, 2, 3]
list2 = [10, 20, 30]

# Here we have 2 lists. Let's say we want to combine these
# two lists into a single list of tuples, like this:
'''
[(1, 10)], (2, 20), (3, 30)]
'''
print(list(zip(list1, list2)))

"""
RESULT:
[(1, 10)], (2, 20), (3, 30)]
"""
# We can actually pass strings as arguments as well:
print(list(zip("abc", list1, list2)))

"""
RESULT:
[('a', 1, 10)], ('b', 2, 20), ('c', 3, 30)]
"""
