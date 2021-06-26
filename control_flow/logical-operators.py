# FUNDAMENTALS OF COMPUTER PROGRAMMING - pt. 4

# Logical Operators
# python has 3 of these: and, or, not

# 1. and

high_income = True
good_credit = True

if high_income and good_credit:
    print("Eligible")
    # BOTH must be true
else:
    print("Not Eligible")

# 2. or

high_income = True
good_credit = True

if high_income and good_credit:
    print("Eligible")
    # ONLY ONE must be true
else:
    print("Not Eligible")

# 3. not

high_income = True
good_credit = True
student = True

if not student:
    # 'not' reverses the value of a boolean
    print("Eligible")
else:
    print("Not Eligible")

# it can get more complex!

if (high_income or good_credit) and not student:
    # only one value in parentheses must be true
    # AND they cannot be a student
    print("Eligible")
else:
    print("Ineligible")

# Python evaluates these in what's called 'short circut'.
# so, one by one, it's next operation completely dependent
# upon the last.
