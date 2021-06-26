# FUNDAMENTALS OF COMPUTER PROGRAMMING - pt. 3

# Ternary Operator

age = 22
if age >= 18:
    print("Eligible")
else:
    print("Ineligible")

# There's a cleaner way to write this code:

age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Ineligible"
print(message)

# when assigning a value to a variable within 'if/else',
# it can all be done in an even SIMPLER way:

age = 22
message = "Eligible" if age >= 18 else "Ineligible"  # The 'Ternary Operator'
print(message)

# Now, that's esentially PLAIN ENGLISH!