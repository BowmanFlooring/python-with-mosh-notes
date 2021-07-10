#--------##--------##--------##--------##--------##--------##--------##--------#

# A Good Example Of Inheritance

# Let's imagine we want to model the concept of a stream of data. That data can
# be sourced from a network, a file, or within memory. But - HOW WE READ THAT
# DATA IS DEPENDENT UPON THE TYPE OF THE STREAM. How we read data from a file is
# different from how we read data from a network.

class Stream:
    def __init__(self):
        self.opened = False
        # So, initially, we are setting the OPENED flag to FALSE - meaning, this
        # STREAM class (stream of data) is closed by default.

    def open(self):
        # In this method, we need to first check if the stream is open. Here's why:
        # If we try to open a stream that's already open, well... that is what's
        # called an 'invalid operation'. We can't do that. So, we need to RAISE an
        # error of some kind. In this case, we can raise a CUSTOM exception! We
        # will simply call it 'Invalid Operation Error'.
        if self.opened:
            raise InvalidOperationError()
        self.opened = True

# Also, we need to head back to the top and create a new class to hold this new
# exception. By convention, ALL custom exceptions must end in 'Error'. So, here
# is our code up to this point:


class InvalidOperationError(Exception):
    # Any time we create a custom exception class, it should derive from the
    # 'Exception' class.
    pass


class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError()
            # Let's give this a friendlly error message as well:
            print("Stream is already open!")
        self.opened = True

# And for the 'close' method:
    def close(self):
        if not self.opened:
            raise InvalidOperationError()
            # Let's give this a friendlly error message as well:
            print("Stream is already closed!")
        self.opened = False

# This code has the common features that we need - in EVERY stream.
# Now, for the GOOD EXAMPLE of inheritance:


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")
