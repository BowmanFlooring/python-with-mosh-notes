# Conditional Statements

tempurature = 35
# After we set our variable, we can use an 'if' statemtent to have
# Python compare some other value against that variable.
if tempurature > 30:
    # Always terminate 'if' statements with a colon
    print("It's warm")
    # We can use 'print' here, as many times as we want!
    #  *as long as it's indented the same as the 'if' statement!*

# We can also add 'elif' (as many "elif's" as needed)
# 'elif' is esentially adding a 2nd condition to the function as a whole.
elif tempurature > 20:
    print("It's nice")
# 'else' prints (or execute) something if everything else above is 'False'
else:
    print("It's cold")
    print("Done")
