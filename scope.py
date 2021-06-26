# Scope

"""
In programming, theres a very important concept 
called 'scope', which refers to the region of the
code in which a variable is defined.
"""


def greet():
    message = "a"

# In this function, the 'scope' of this variable ("a"),
# is within the 'greet' function. The variable only exists
# within that function.
# So, if we try this:


print(message)

# Notice, since it's outside of the function, we get
# the underline. And if we try to run it, we get:
# NameError: name
# 'message' is not defined

# The same rule applies to the parameters of our functions.


def greet(name):
    message = "a"


print(name)

# Again, same underline, same Traceback error in the terminal.

# So, the scope of the 'name' and 'message' variable are
# the 'greet' function, and we refer to these variables
# as 'local variables' to this function. They're local in this
# function.
# This means we can have multiple variables with the same name,
# as long as they exist within different functions.
# Example:


def greet(name):
    message = "a"


def send_email(name):
    message = "b"

# These two 'message' variables are totally separate from eachother
# Local variables have a short life.

# In contrast to local variable, we have...

# Global Variables

# If we move the message variable outside of the 'greet' function,
# it's now a 'global variable', and that makes is accessible
# ANYWHERE within this file.


#message = "a"


def greet(name):
    message_1 = "c"


def send_email(name):
    message = "b"


greet("Dakota")

# Because the scope of global variables is the entire file, they
# stay in memory for a much longer period of time.
# For this reason, global variable really should NOT be used
# all that often. Instead, as a best practice, create functions
# with parameters and local variables.


# BAD PRACTICE EXAMPLE:

message = "a"


def greet(name):
    # Some devs will MODIFY this local variable with 'global'
    global message
    message = "b"


greet("Dakota")
print(message)

"""
So, some of these 'not-so-great' developers will modify the
local variable with the 'global' function. 

THIS IS A HORRIBLE IDEA!!!
DO NOT EVER DO THIS!!!

Some of our defined functions may rely on that variable and,
as a result, this could cause major bugs within our code.
We don't want that. Ever.

Thanks, Mosh. :)
"""
