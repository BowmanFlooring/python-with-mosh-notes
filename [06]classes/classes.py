# Classes

# Classes are not only important in Python, but programming in general!
# Let's start with an example:

numbers = [1, 2]
# 'numbers' is a 'list object'. All list objects have a certain list of methods,
# which are accessible to the object when called via dot notation, like:
numbers.append()
numbers.sort()
numbers.insert()
numbers.pop()
numbers.reverse()
# ...and so on....

# So, for example:
x = 1
print(type(x))
# We get 'class <int>' - this 'int' class is a class for creating integers. There
# are many classes in Python - boolean, string, list, dictionary, etc...

# EVERY OBJECT IN PYTHON IS CREATED USING A CLASS.

# Let's define a few terms:
'''
CLASS: A blueprint for creating new objects.
Object: An instance of a class.

For example, we could create a class, and call it
'Human'

In that class, we could creates objects that would be 
attributes of that class, like
'John', 'Mary', 'Jack', etc.

You may hear people use these terms interchangably - this is wrong! 
'Class' and 'Object' are two different terms.
'''
