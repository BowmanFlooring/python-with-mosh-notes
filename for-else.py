# For..Else

successful = True 
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        # to jump out of loop, use 'break'
        break 

# perhaps we want to display a message if 3 tries and still nothing

successful = False 
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        # to jump out of loop, use 'break'
        break 
else:
    print("Attempted 3 times and failed!")

# the else statement will only execute if we NEVER break
# out of the 'for' loop.
# in this example, the 'else' statement WOULD execute.
# if we changed 'successful' to 'False', it WOULDN'T.
