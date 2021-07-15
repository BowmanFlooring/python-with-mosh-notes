# This is the last video of this section, so i decided to give
# it it's own folder.

# NumPy
import numpy as np
# We can now use 'np' in place of 'numpy'. It's shorter. Let's
# return an array:
array = np.array([1, 2, 3])
print(array)
'''
RESULT: [1 2 3]
'''
# This is actually called a 'numpy' array. Let's print it's type:
print(type(array))
'''
RESULT: <class 'numpy.ndarray'>
'''
# Now, let's create a two-dimentional array (matrix):
array = np.array([[1, 2, 3], [4, 5, 6]])
print(array)
'''
RESULT:
[[1 2 3
  4 5 6]]
'''
# So now we have a 2D array with 2 rows and 3 columns. To prove
# this, try this:
print(array.shape)
'''
RESULT: (2, 3) <-- This is the number of items per direction.
'''
# Here's a few more tricks:
array = np.zeros((2, 3), dtype=int)
array2 = np.ones((2, 3), dtype=int)
array3 = np.full((2, 3), 9, dtype=int)
print(array)
print(array2)
print(array3)
'''
RESULT:
[[0 0 0]
 [0 0 0]]
RESULT2:
[[1 1 1]
 [1 1 1]]
RESULT3:
[[9 9 9]
 [9 9 9]]
'''
