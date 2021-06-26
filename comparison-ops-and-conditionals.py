# FUNDAMENTALS OF COMPUTER PROGRAMMING - pt. 1

# Comparison Operators

10 > 3  # is greater than
10 >= 3  # is greater that or equal to'
10 < 20  # is less than
10 == 10  # 'is equal to'
10 == "10"  # False ("10" is a string, 10 is an integer)
10 != "10"  # True

"bag" > "apple"  # True
"bag" == "BAG"  # False
ord("b")  # <-- 98
ord("B")  # <-- 66

# FUNDAMENTALS OF COMPUTER PROGRAMMING - pt. 2

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
