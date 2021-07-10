#--------##--------##--------##--------##--------##--------##--------##--------#

# Duck Typing

from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()

# Is the same thing as:


class TextBox:
    def draw(self):
        print("TextBox")


class DropDownList:
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()

# Python is a dynamically typed language. We don't necessarily have to define
# a UIControl class. Lines 41-43 are the important bits. Within that draw
# function, as long as we are iterating over that controls parameter AND we
# have a draw method, Python is happy.

# "If it walks like a duck, and quacks like a duck, it IS a duck."

# Python doesn't look for the kinds of objects; it only checks the existence
# of certain methods defined within those objects. For example, on line 16, if
# Python detects the existence of a draw method, it assumes it's a UI control.
# That's how Python works. Polymorphic behavior will still be achieved in our
# second example - JUST LIKE the first example, but with way less typing.
# It's done with 'Duck Typing' :)

# NOTE: Even though it's not necessary, having 'UIControl' as an abstract base
# class is still a good practice; it enforces that 'common interface' or a
# 'common contract' across all it's derivitives. It will make sure that they
# all WILL have a draw method.
