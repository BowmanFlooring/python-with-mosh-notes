#--------##--------##--------##--------##--------##--------##--------##--------#

# Extending Built-in Types

# In Python, we can also use inheritance with the built-in types. For example,
# if we create a class called 'Text', and derive it from the 'str' (string)
# built-in class, it will have all the features of strings. Then, we can just
# add more features to it. Kind of like a 'souped-up' version of strings:

# For a simple example, we can add a 'duplicate' feature to our 'Text' class:
class Text(str):
    def duplicate(self):
        return self + self


text = Text("Python")
print(text.duplicate())
'''
RESULT: PythonPython
'''
# Pretty Useful!

# In another example, we can also extend Python's lists:


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)


list = TrackableList()
list.append("1")
'''
RESULT:
Append called
'''
