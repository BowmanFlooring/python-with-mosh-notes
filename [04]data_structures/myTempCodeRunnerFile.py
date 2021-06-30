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