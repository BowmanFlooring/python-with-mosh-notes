#---10----#---20----#---30----#--40---#••#---50--#----60---#----70---#----80---#

# Properties

# Properties can simply be looked at as control over a certain attribute within
# a class. Sometimes, just defining the attribute isn't enough for the real-
# world application of the code to work as planned. For example, here's some
# code - we are defining a class, 'Product', and within the classes constructor,
# we've set the 'price' attribute. With this specific implementation, we can
# actually create a product object and give it a NEGATIVE value. This this NOT
# ideal. Nor is it possible. Also, it set's the stage for bad code-writing
# habits in the future. Here's the code:
class Product:
    def __init__(self, price):
        self.price = price


product = Product(-50)
print(product.price)
'''
RESULT: -50
'''

# There are a couple ways to fix this. For the first fix, we could set the
# 'price' attribute to private[1]:


class Product:
    def __init__(self, price):
        self.__price = price
#  then, we set two methods within the class: one for getting the price, and
# one for setting it.

    def get_price(self):
        return self.__price

    def set_price(self, value):
        # As a HIGHLY SUGGESTED optional, we could throw an 'if' statement on the
        # 'set' method, raising a 'ValueError' exception if att. is below 0:
        if value < 0:
            raise ValueError("Price cannot be negative!")
            # We would refer to this 'if' statement as
            #       **DATA VALIDATION LOGIC**
        self.__price = value

# Now, in a second implementation, we could just ignore setting the value com-
# pletely if it's set at anything less than zero.

# Let's go back to the first implementation. Now, if we go back up the our
# contructor - instead of directly setting the 'price' (or '__price') attribute,
# we can call 'self.set_price(price)', with '(price)' being the initial value:


class Product:
    def __init__(self, price):
        self.get_price(price)
# So if we run this, our data validation logic will kick in, and our exception,
# "ValueError", will get thrown along with our print statement.


# That's great and all - but it's not "Pythonic". When the upper echelon of the
# active python community uses this term, they mean that the code just isn't
# quite using Python to it's fullest extent - or potential. To quote Mosh:
#
# "This is code that a Java programmer learning Python would write"
#
# LOL. A "Pythonic" fix would be to use what's called a property. A property is
# an object that sits in front of an attribute and allows us to get or set the
# value of said attribute. Using a property here would be more Pythonic because
# we are using a complex builtin feature-set of Python - and before, we were
# doing the same thing, just taking a wayyy longer route to get there. So,
# let's introduce a property into our code:

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be less than 0!")
        self.__price = value


# NOTE: When defining a property, you don't always have to have a price setter
# and a price getter.
#---10----#---20----#---30----#--40---#••#---50--#----60---#----70---#----80---#
'''
REFERENCE(S):
----------
[1] refer back to 'private-members.py' for details
'''
