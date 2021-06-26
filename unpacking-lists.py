# Unpacking Lists

# assigning an item in a list to a variable:
numbers = [1, 2, 3]
first = numbers[0]
second = numbers[1]
third = numbers[2]

# we can do this much, much easier:
first, second, third = numbers

# It's important to note that the number of variables on the
# LEFT SIDE of the '=' operator MUST BE EQUAL TO the number
# of items in the list. Otherwise, 'ValueError:' in terminal!

# we can use an asterisk to pack some of the list into a variable
# This works just like the examples from 'xargs'.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first, second, *other = numbers
print(first)
print(second)
print(other)

# RESULT
# 1
# 2
# [3, 4, 5, 6, 7, 8, 9]

# If we put '*other' in the middle, we can now obtain the values
# at each end of the list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first, *other, last = numbers
print(first, last)

# RESULT
# 1 9
