#--------##--------##--------##--------##--------##--------##--------##--------#

# Method Overriding
# DEFINITION: Replacing OR Extending a method defined in the base class.
class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        self.weight = 2

    def walk(self):
        print("walk")


m = Mammal()
print(m.age)
print(m.weight)

# When running this code, we get an 'Attribute Error'. The CONSTRUCTOR of the
# base class, ANIMAL, was OVERRIDDEN by the CONSTRUCTOR of the subclass, MAMMAL.

# Here's the fix (done within the SUBCLASS CONSTRUCTOR):


class Animal:
    def __init__(self):
        print("Animal Constructor")  # Added to test fuctionality!!
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        # Calling this 'super()' function gives access to the SUPER/BASE
        # class - which, in this case, is ANIMAL.
        print("Mammal Constructor")  # Added to test functionality!!
        self.weight = 2

    def walk(self):
        print("walk")


m = Mammal()
print(m.age)
print(m.weight)
"""
RESULT:
Animal Constructor
Mammal Constructor
1
2
"""

# NOTE: To change the order, all you need to do is simply move the calling
# of the 'super()' function to the bottom of the constructor!! :)
