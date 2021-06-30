# Sets

# Sets are a super useful data structure in Python. A set is a
# collection of items with no duplicates.

# So, with that knowledge, let's define a list and purposely add
# a duplicate:
numbers = [1, 1, 2, 3, 4, 5]
# We can transform this list to set very simply:
uniques = set(numbers)
print(uniques)
'''
RESULT:
{1, 2, 3, 4, 5}
'''

# Notice, the result is surrounded with curly braces. So, a set is
# a) unique
# b) defined within curly braces

# With that information, let's make a new set:
second = {1, 4}
# Now, let's add an item, then check:
second.add(3)
print(second)
'''
RESULT:
{1, 3, 4}
'''
# Then, remove one - again, checking it after:
second.remove(1)
print(second)
'''
RESULT:
{3, 4}
'''
# To get the length of the set:
print(len(second))
'''
RESULT:
2
'''
# We can also merge two sets by using a verticle bar. This union
# of sets outputs a new set with all unique items from the given
# sets:
set_one = {5, 11, 23, 44, 89}
set_two = {23, 44, 61, 73}
print(set_one | set_two)
'''
RESULT:
{5, 73, 11, 44, 23, 89, 61}
'''
# We can get the intersection of two sets with the ampersand
# operator. This will tell us what the duplicate items are:
print(set_one & set_two)
'''
RESULT:
{44, 23}
'''
# We can get the difference between two sets:
print(set_one - set_two)
s = 1
