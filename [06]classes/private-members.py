#------------------------------------------------------------------------------#

# Private Members

# So - our code from the last lecture, our 'TagCloud' class, has a bit of a
# prolem. Let's check it out again:
class TagCloud:

    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("python")
print(cloud["PYTHON"])
'''
RESULT: 3
'''
# THIS IS CORRECT. BUT - what if we do this?:
cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("python")
print(cloud.__tags["PYTHON"])
'''
RESULT: Traceback ........ KeyError: 'PYTHON'
'''

# The problem is this: on this second attempt, we tried to access to dictionary
# we have stored in memory. Remember, we've created an attribute within our
# class to automatically force the tags to lowercase, for easier recalling and
# such. Here's a fix:

# In our code, all of the '.tags', we change to '.__tags' - this hides that
# specific attribute and makes it very hard to access! But not impossible.
# Esentially, this is used as a worning to anyone, saying 'hey, don't touch this'
# or 'don't mess with this'.

# Again, accessibility of these types of items are difficult. Every class, by
# default, has this property called '__dict__'. This is a dictionary that holds
# ALL the attributes in this class. Let's give it a test run and see what we get:
print(cloud.__dict__)
'''
RESULT: {'_TagCloud__tags': {}}
'''
# This '_TagCloud__tags' item is pointing to an empty dictionary.
# So, unlike a lot of other languages, Python doesn't really have this concept
# of 'Private Members'. These items are still 'technically' accessible. This
# 'double underscore' method is more of a practice to prevent accidental access
# of these 'Private Members'.
