# While Loops
# use these to repeat something as long as a condition is true

# evaluate condition, repeat task. like:

number = 100
while number > 0:
    print(number)
    number //= 2

# RESULT
# 100
# 50
# 25
# 12
# 6
# 3
# 1

# a terminal shell is an example of a while loop!
# here's a simple one:

command = ""
while command != "quit":
    command = input(">")
    print("ECHO", command)
    # this will execute until we type 'quit'

# problem: they can't type 'QUIT', or 'Quit'.
# Let's fix that!...:

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

# we comvert the command to lowercase, that way
# NO MATTER HOW THEY TYPE IT, it will always get converted 
# to all lowercase anyways!
