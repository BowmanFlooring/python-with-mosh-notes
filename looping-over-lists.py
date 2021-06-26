# Looping Over Lists

# We can use a for loop to loop over a list.
letters = ["a", "b", "c"]
for letter in letters:
    print(letter)
"""
RESULT:
a
b
c
"""
# We can build a Tuple from a list as well.
# For this, we will use the builtin 'enumerate' function.
letters = ["a", "b", "c"]
for letter in enumerate(letters):
    print(letter)
"""
RESULT:
(0, 'a')
(1, 'b')
(2, 'c')
"""
# In each Tuple built, the first item is the INDEX of it's pair.
# So now, to get the index, we can use the square brackets to
# access the first item in this tuple.
# then, beside that, we can use square brackets with [1] beside
# it and we will see the item at a given index.
letters = ["a", "b", "c"]
for letter in enumerate(letters):
    print(letter[0], letter[1])
"""
RESULT:
0 a
1 b
2 c
"""
# That syntax is ugly.In the last lecture, we learned
# about 'list unpacking. We can unpack the list into
# 2 variables, like this.
letters = ["a", "b", "c"]
items = [0, "a"]  # This can be either '()' or '[]'
index, letter = items
for index, letter in enumerate(letters):
    print(index, letter)
"""
RESULT:
0 a
1 b
2 c
"""

# TO RECAP
"""
: We can use 'for' loops to iterate over lists.
: If you also need the index, call the 'enumerate' function,
  which will return an enumerate object, which is iterable.
  In each iteration, it will return a 'tuple', and you can
  unpack that tuple in variables. 
        
        Ex: index, letter = items 
"""
