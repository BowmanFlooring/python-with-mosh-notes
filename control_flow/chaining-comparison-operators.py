# Chaining Comparison Operators

# age should be between 18 and 65

age = 22
if age >= 18 and age < 65:
    print("Eligible")

# in math, we would write:

18 <= age < 65

# guess what? in Python, is the same! so:

age = 22
if 18 <= age < 65:
    print("Eligible")

# QUIZ

if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")

# What will print???
# Answer: c !!!!
