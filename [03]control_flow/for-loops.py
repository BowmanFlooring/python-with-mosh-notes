# For Loops

print("Sending a Message")

for number in range(3):
    # This is saying 'repeat it 3 times'.
    # again, terminate with a colon!
    print("Attempt", number)

# This would print:
# Attempt 0
# Attempt 1
# Attempt 2

# adding '+ 1' to 'number' in the 'print' statement:

for number in range(3):
    print("Attempt", number + 1)

# This would print:
# Attempt 1
# Attempt 2
# Attempt 3
# This is more "user friendly"

# something else to add....:

for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")

# Attempt 1 .
# Attempt 2 ..
# Attempt 3 ...

# something more....:

for number in range(1, 4):
    print("Attempt", number, number * ".")

# This eliminates having to add '+1' every time!

# and more, again...:
# if we pass a 3rd argument to 'range', it becomes the step:

for number in range(1, 10, 2):
    print("Attempt", number, number * ".")

# This prints:
# Attempt 1 .
# Attempt 3 ...
# Attempt 5 .....
# Attempt 7 .......
# Attempt 9 .........

