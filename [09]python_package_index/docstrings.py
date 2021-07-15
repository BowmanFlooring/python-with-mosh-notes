# -------------------------------------------------------------------------------

# Docstrings

# Docstrings are strings of text within our code that describe the classes,
# modules, functions, etc. of our custom-written code. Nobody like to use code
# from libraries that aren't well-documented! As an added benefit, if you use the
# "VSCode" IDE (or other IDE's I'm sure), you'll see the docstrings come up as
# descriptions while typing! So, let's write a basic class, and include docstring
# data within. Here's what that looks like:
""" This module provides functions to convert *something* to *something else*. """


class Converter:
    """ A simple converter for converting blah to blah. """

    def convert(self, path):
        """
        Convert the given blah to blah.

        Parameters:
        path (str): The path to a given blah.

        Returns:
        str: The content of the blah as blah.
        """
        print("Simple docstring test.")

# Docstrings MUST be encapsulated in triple quotes. For descriptive clauses, the
# first line should be a SHORT descriptor. If we want to add more of an in-depth
# explanation, SKIP A LINE - then write the in depth description. Also, In the
# docstring within the 'convert' method from above, notice a few things. First,
# It starts on a completely new line - that's optional. Just remember to always
# leave a space between the text and the triple quotes if you don't skip a line.
# Second - after each section in the docstring, we are skipping a line. That is
# NOT optional. Do it - ALWAYS. As far as content goes, always include required
# parameters (if any) and what the method/function returns.

# Now, this file can be imported into another '.py' file just as if it were a
# typical Python module - like 'pathlib' or 'datetime', etc... and when the
# words in the module are typed, the IDE (in this case, VSCode) will recognize
# them and provide the descriptions however the settings specify. Nice!! :)
