# Strings

# Strings are referred to as a 'string' of characters,
# encapsulated in either doulbe- or single-quotes.

# Use double quotes to enclose strings, like:
course = "Python Programming"

# Use single quotes to enclose strings, like:
course = 'Python Programming'

# Single quotes CAN be used, but double quotes are the
# generally preferred usage.

# use triple quotes for strings spanning multiple lines, like:
course_description = """
Hello, and welcome to the course!
I'm your instructor, Mosh.
This course will teach you all you
need to know about Python. Hopefully
by the end, you'll be 100% satisfied!
"""
# --------------------
# NOTE:

# Mosh doesn't mention this, but it's worth discussing:

# The 'triple-quotes' are convenient for "commenting out" a
# bunch of text when you don't want to actually prepend every
# single line with (#'s), like:
"""
You can put anything you want here! Notice, since Python
recognizes this as a 'string', and not a comment, it's also
a different color, which has a couple useful applications.

You can think of this type of a string as a 2nd
type of comment for your code. For example, let's imagine
you're writing a tutorial-style game-building program geared
towards beginners in Python. You could assign '#'-type 
comments to developers, and 'string-type' comments to the
actual students.

Although you may not be using the same editor/IDE that I've 
chosen to use, it's likely that whatever you ARE using has
some form of syntax highlighting for Python. If not, please
switch now! This course goes into pretty good detail about
editors and IDE's. Mosh even walks you thru the download and
install process for most of them - INCLUDING the DL/INST 
process for linters and other language-specific tools.

Also, be aware that Python still evaluates this as a string
at runtime. So, even though we haven't assigned it to any
one specific variable, it's still in Python's executable
path. This means it will take up some amount of memory. 
More importantly, if you're running a program in which you
must calculate time taken up by a certain function, then 
using this as a comment is not advisable, considering it's
an actual string, and it will be factored in to the total
evaluated runtime - whereas commenting lines out with '#'
are simply ignored by Python altogether.

                    RANT OVER :)
"""
