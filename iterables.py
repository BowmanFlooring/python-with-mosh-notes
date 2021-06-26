# Iterables

print(type(5)) # class 'int'
print(type(range(5))) # class 'range'

# range objects are 'iterable', meaning 
# they can be used in 'for' loops

# Strings are iterable
for x in "Python":
    print(x)

# RESULT
# P
# y
# t
# h
# o
# n

# lists are also iterable:
for x in [1, 2, 3, 4]:
    print(x)

# RESULT
# 1
# 2
# 3
# 4

# later, we will see how to make custom iterables:
for item in shopping_cart:
    print(item)