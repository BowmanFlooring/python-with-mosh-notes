#--------##--------##--------##--------##--------##--------##--------##--------#

# Abstract Base Classes, pt. 2
# We need to turn our 'Stream' class into an abstract base class. To do that,
# we need to import a couple classes from the 'abc' module (builtin).
from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


# Once imported, our 'Stream' class needs to be derived from the "ABC" class:
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
# Here is where we will define the COMMON INTERFACE for ALL stream classes.
# For now, just 'read'. Potentially a 'write' method in the future. Also,
# we need to DECORATE this method with '@abstractmethod', while also making
# the method have NO implementation (use 'pass'):

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file...")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a stream...")

# NOTE: ALL 'STREAM' CLASSES MUST HAVE A DEFINED 'READ' METHOD NOW. THIS IS
# BECAUSE WE HAVE CREATED A COMMON INTERFACE FOR ALL STREAM CLASSES. SO, IF A
# CLASS DERIVES FROM OUR 'STREAM' CLASS, WE WILL NOT BE ABLE TO INSTANTIATE THAT
# CLASS (MAKE AN INSTANCE OF IT) UNLESS IT HAS A DEFINED READ METHOD!
