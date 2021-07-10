#--------##--------##--------##--------##--------##--------##--------##--------#

# Multiple Inheritance

# Again, this can be a huge source of issues!

class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


class Manager(Employee, Person):
    pass


manager = Manager()
manager.greet()
'''
RESULT: Employee Greet
'''
# So, what Python does here is this:
# We call the 'greet' method with dot notation. Python looks at the Manager class FIRST,
# because that's the class we've called the method on. If there's no greet method in that
# class, it tries the EMPLOYEE class - we have the employee class referenced as a base
# class BEFORE the PERSON class. Since there's a GREET method within the EMPLOYEE class,
# Python is done looking.

# The concept of multi-level and multiple inheritance is mostly a bad thing - so why does
# Python have it as a feature? Well, if used 100% correctly, it can be a good thing!
