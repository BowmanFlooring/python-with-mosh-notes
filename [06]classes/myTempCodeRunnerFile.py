class TagCloud:
    
    def __init__(self):
        self.tags = {}
    
    def add(self, tag):
        # Right Here: To handle case sensitivity, we need to convert the tag
        # to lowercase when setting it, and also when reading it. 
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1


cloud = TagCloud()
# Let's mess with the letter cases here, just to test our implementation:
cloud.add("pYtHon")
cloud.add("PythoN")
cloud.add("pyTHOn")
print(cloud.tags)
'''
RESULT:

'''
