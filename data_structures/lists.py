# Lists

letters = ["a", "b", "c"]  # A list of objects
matrix = [[0, 1], [2, 3]]  # A 'matrix' - 2 dimentional list

# Say we want a list of 100 0's.
# we use an asterisk to repeat the items in a list:
zeros = [0] * 100
print(zeros)

# similarly, we can use '+' to concatenate multiple lists
combined = zeros + letters

# say we want a list of numbers, 0 - 20
numbers = list(range(20))
print(numbers)

# or, we can list out characters in a string
chars = list("Hello World")
print(chars)

# or even get the length of a list
print(len(chars))
