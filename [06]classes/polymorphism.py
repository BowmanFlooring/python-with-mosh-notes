#--------##--------##--------##--------##--------##--------##--------##--------#

# Polymorphism

from abc import ABC, abstractmethod

# This class is our abstract base class. As you can see from it's 'draw' method,
# it has NO implementation. So, this class ONLY defines the CONTRACT, or the
# COMMON INTERFACE with which all it's derivitives must adhere.


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass

# Below, we have two classes, both derivitives of the 'UIControl' class. BOTH
# classes implement the 'draw' method. In both implementations, they simply
# print their class names, respectively


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


# Now, here we also have a function called 'draw' that takes a UI control
# object, and calls the 'draw' method on it.
def draw(control):
    control.draw()


# So we can now create a 'DropDownList' object, and pass it to this 'draw'
# function, like this:
ddl = DropDownList()
draw(ddl)

# This should be just fine, because 'DropDownList' is an INSTANCE of the
# 'UIControl' class. Just to verify the 'truthiness' of that theory, let's
# call the 'isinstance' object, and pass in 'ddl' and 'UIControl', like this:
print(isinstance(ddl, UIControl))
'''
RESULT: True
'''
# Remember, the 'isinstance' object - when given two arguments - will check
# to see if the first argument is an instance of the second argument.

# THIS MEANS THAT WHEREVER WE EXPECT A UICONTROL OBJECT, WE CAN PASS ANY OF
# IT'S DERIVITIVES - LIKE 'TEXTBOX' OR 'DROPDOWNLIST'.

# So, back up top, from {line 34-41}:
ddl = DropDownList()
draw(ddl)
'''
RESULT: DropDownList
'''
# Now, let's try the same thing with our 'TextBox' object:
textbox = TextBox()
draw(textbox)

# What's the point of this? Well, what if we want to return a list, or a
# tuple of controls? Let's do this:


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
textbox = TextBox()
draw([ddl, textbox])
'''
RESULT:
DropDownList
TextBox
'''

# Using this approach, we can render the user interface of an application,
# all within the 'draw' function. In another scenario, we could pass in more
# drop down lists, radio buttons, etc. - and again, the entire UI would be
# rendered with that 'draw' function.

# The 'draw' function doesn NOT know what kind of controls it's working with
# here. That is determined at runtime. It's simplying iterating over 'control'
# and calls the 'draw' method on each 'control' object.
# THIS IS CALLED POLYMORPHISM!
# Poly = many
# Morphism = forms
# Polymorphism = many forms
