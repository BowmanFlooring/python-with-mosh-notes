# Accessing Items


letters = ["a", "b", "c", "d"]
print(letters[0])
# this returns the first item in the list.

print(letters[-1])
# this returns the first item from the END of the list

# we can change items within the list as well:
letters[0] = "A"
print(letters)

# RESULT
# ['A', 'b', 'c', 'd']

# we can slice strings as well
print(letters[0:3])

# and even pass a 'step', like:
print(letters[::2])

# RESULT
# ['A', 'c']

# Here's a better example of stepping a list:
numbers = list(range(20))
print(numbers[::2])

# RESULT
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Another:
print(numbers[::-1])

# RESULT
# [19, 18, 17, 16, 15,
#  14, 13, 12, 11, 10,
# 9, 8, 7, 6, 5, 4, 3,
# 2, 1, 0]
