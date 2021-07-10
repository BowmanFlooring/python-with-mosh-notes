#--------##--------##--------##--------##--------##--------##--------##--------#

# Multi-Level Inheritance

class Animal:
    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("fly")

# Here, we now know just by looking at this code that the BIRD class will
# INHERIT the EAT method from the ANIMAL class. But, as we start to write more
# amd more complex lines of code, too much inheritance can cause all kinds of
# undesirable issues within. So, let's define a new class:


class Chicken(Bird):
    pass
    # This does nothing (placeholder). In Python, we cannot have a class
    # with nothing in it, so this satisfies that logic for Python.

# This type of generalization and multi-level inheritance should be avoioded
# at all costs. Simplify it!!!
