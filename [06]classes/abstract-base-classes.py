# %%
#--------##--------##--------##--------##--------##--------##--------##--------#

# Abstract Base Classes

class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream already open!")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream already closed!")
        self.opened = False


class FileStream(Stream):
    def read(self):
        print("Reading data from a file...")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a stream...")


# There are a couple issues with this type of implemetation. First,
# we can create a 'stream' object, and call the 'open' method:
stream = Stream()
stream.open()

# Why is this an issue? Well, our 'open' method is what's called an
# ABSTRACT CONCEPT. What does it mean to 'open a stream'? So, because of
# this, we should not be able to directly create an INSTANCE of the STREAM
# class. It should not be able to be INSTANTIATED. We should always create
# a SUBCLASS, then create an instance of the subclass!

# Secondly - If, say, tomorrow we decide to make another type of 'stream'
# class, we have to remember to make a 'read' attribute, and call it
# exactly how it's called in all other stream classes (read). Otherwise,
# it's not going to have consistency within the code.
# IN OTHER WORDS: There is currently no way to enforce a COMMON INTERFACE
# across different kinds of streams. In order to fix that, we must create and
# use an ABSTRACT BASE CLASS. These types of classes are NOT meant to be used
# directly. Their goal is to provide some common code to their derivitives.

# NOTE: CONTINUED IN PART 2!
