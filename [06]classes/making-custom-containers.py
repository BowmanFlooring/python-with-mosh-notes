#--------##--------##--------##--------##--------##--------##--------##--------#

# Making Custom Containers

# Earlier in the course, we learned about multiple different data structures -
# list, sets, dictionaries, etc. These are all referred to as 'container types'.
# Those container types are going to be used for most things we need them to do,
# but in some instances, we may want to create our own CUSTOM CONTAINER TYPES:

# We are going to custom-build a container-type, and it will contain the number
# of various tags on a blog. For example - how many articles do we have that are
# tagged with 'Python3', 'Javascript', 'MySQL', 'Django', 'PHP', 'MongoDb', etc.

+class TagCloud:

    # Because this class is a container, it supports various operations involving
    # containers. Here are those operations:

    # Get the number of items in this container:
len(cloud)
# Get an item by it's key, and also set it:
cloud["python"] = 10
# We can also INTERATE over that container (lists are ITERABLE!)
for tag in cloud:
    # Print each tag
    print(tag)

#--------##--------##--------##--------##--------##--------##--------##--------#

# Mosh's 'from the bottom up' implementation of a class like this:


class TagCloud:
    # Internally (within our class), we will be using one of the built-in date
    # structures - lists, dict's, etc. In this case, we will use a dictionary,
    # because it will allow us to easily get the nymber of a given tag.
    def __init__(self):  # <- remember, this is our 'constructor'
        self.tags = {}  # <- let's set the 'tags' attribute to an empty dict.

    # Now, we can optionally add a method that takes a tag:
    def add(self, tag):
        # Here, we should check to see if we have this tag in our dictionary. If
        # we don't, set the value of the tag to 1 - otherwise, increment by 1
        # So, if we call upon this tag, and it doesn't yet exist, we will now
        # have one tag in our dictionary with whatever name is specified. If we
        # already have that specific tag in our dictionary, we simply increase
        # that tag's count by one - so, there would now be one more tag of that
        # specific name. Pretty simple. Here's one way to implement that code:
        self.tags[tag] = self.tags.get(tag, 0) + 1


# And finally, let's pass a reference to the 'TagCloud' class, then call it's
# 'add' method 3 times - just to test our implementation of the 'add' method.
cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("python")
# When we print the result, we get:
print(cloud.tags)
'''
RESULT:
{'python': 3}
'''
# So, it's saying "the 'python' tag is in our system 3 times".

#--------##--------##--------##--------##--------##--------##--------##--------#

# Now, you may wonder: "why not just use a plain `ole dictionary?!" Well, if
# we create a class, like so, we can esentially build out a dictionary that
# is much, much smarter than a 'plain `ole dictionary' For example, say we
# want to handle 'CASE SENSITIVITY' - in a normal dict. object in Python,
# 'Python' and 'python' are recognized separately. By default, it will be
# executed as such within our class, as is. To implement 'case INsensitivity,
# we need to write in some code:


class TagCloud:

    def __init__(self):
        self.tags = {}

    def add(self, tag):
        # Right Here: To handle case sensitivity, we need to convert the tag
        # to lowercase when setting it, and also when reading it.
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1


cloud = TagCloud()
# Let's mess with the letter cases here,
# just to test our implementation:
cloud.add("pYtHon")
cloud.add("PythoN")
cloud.add("pyTHOn")
print(cloud.tags)
'''
RESULT:
{'python': 3} <-<-|\\\\| BEAUTIFUL! It's  been converted to lowercase |\\\\|
'''
# In doing this, all the complexity of the rules we've defined around case
# sensitivity is strictly encapsulated within the 'TagCloud' class - it's not
# going to muddy up the rest of our code base, we can make the easy one-line
# references to the beginning/end of the code, etc. It's not visible to the rest
# of our program, this slowing things down; clogging things up.

#--------##--------##--------##--------##--------##--------##--------##--------#

# Let's add the ability to get the 'count' of a tag, using square brackets,
# like this: cloud["python"] -- To do this, we need to implement a mogic
# method called '__getitem__'. Let's bring down the code once more:


class TagCloud:

    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)
    # With this current implementation of '__getitem__', we can only READ the
    # item. We cannot SET it. To do this, we have to implement yet another
    # magic method, called - you know it! - '__setitem__'. This magic method
    # take three (3) parameters - self, key, value. In this case, our 'key'
    # is 'tag', and our 'value' is 'count':

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count
    # Now, in order to get the number of items in this tag cloud, we need to
    # again import a magic method - '__len__':

    def __len__(self):
        return len(self.tags)
    # And FINALLY, to make this ITERABLE - so we can iterate over it with a
    # 'for' loop - we need to import one more magic method, '__iter__'.

    def __iter__(self):
        # Now, here, all we have to do is use one of the built-in functions
        # to get an 'iterator object'. An iterator object is an object that
        # "walks" a container, and gets one item at a time. So, we call
        # 'iter', which is one of the built-in functions. Just to ve clear,
        # we want to ITERATE over 'self.tags'. This function returns itera-
        # tor object, which gives us one item at a time, in a 'for' loop.
        # So, simply return it.
        return iter(self.tags)

#--------##--------##--------##--------##--------##--------##--------##--------#


'''
NOTE: 
    DON'T FORGET!
    
    As we progress further along in the course, the actual code may start to
    get a bit hard to discern. I've made up a 'just_the_code' directory that
    is nested within every course category (including the entry-level dirs
    at the beginning!). In that directory, you will find an exact copy of all
    the filenames from the directory it's nested into - but with one major
    difference....
                            ..NO NOTES....

                                .....Just the code...

    It cuts out all the b.s., and get's right to the point. Are they all 100%
    executable, without fail? Of course not! But they're 100% copy-pastable,
    ready to be turned in to snippets - or love letters. Whatever works, man.

    Again, thanks!  


    {
    dakota bowman, founder/coo - bfc©
    shannon bowman, owner/ceo - bfc©
    }

'''
