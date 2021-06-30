#------------------------------------------------------------------------------#
 ###  ***LAST LECTURE BEFORE 'EXERCISE' FOR THE SECTION OF THE COURSE!***   ###

# Unpacking Operator

numbers = [1, 2, 3]
print(numbers)
'''
RESULT:
[1, 2, 3]
'''
# But, what if we don't want to see any outputted notation (commas, paren.)?
print(1, 2, 3)
print(*numbers)
'''
RESULT:
1 2 3
'''
#

values = list(range(5))
values = [*range(5)]
values = [*range(5), *"Dakota"]
print(values)
'''
RESULT:
[0, 1, 2, 3, 4, 'D', 'a', 'k', 'o', 't', 'a']
'''

# Using this operator, we can combine multiple lists:
first = [1, 2]
second = [3]
values = [*first, *second]
print(values)
'''
RESULT:
[1, 2, 3, 4] 
'''

# We can even get a little creative...:
first = [1, 2]
second = [3, 4]
values = [*first, "a", *second, *"Hello"]
print(values)
'''
RESULT:
[1, 2, 'a', 3, 4, 'H', 'e', 'l', 'l', 'o']
'''

# And as for dictionaries:
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 38}
print(combined)
'''
RESULT:
{'x': 10, 'y': 2, 'z': 38}
'''


'''
....................
.........  .........
........    ........
.......      .......
......        ......
.....  *NEXT*  .....
......        ......
.......      .......
........    ........
.........  .........
....................
....................
.........  .........
........    ........
.......      .......
......        ......
.....  *QUIZ*  .....
......  !!!!  ......
.......      .......
........    ........
.........  .........
....................
'''