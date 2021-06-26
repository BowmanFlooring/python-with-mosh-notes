# Formatted Strings

# Ex.1:
first = "Dakota"
last = "Bowman"
full = first + " " + last  # <-- this is called 'concatenation'
print(full)
# RESULT:
# Dakota Bowman

# Ex.2:
first = "Dakota"
last = "Bowman"
full = f"{first} {last}"
print(full)  # <-- again, the print = Dakota Bowman
# RESULT:
# Dakota Bowman

# this is a "formatted string"
# This example keeps simple OR complex code much cleaner-looking.
# At runtime, Python just replaces everything in curly braces,
# & the space remains a space. so, we could put any expression(s)
# within those curly braces and receive it's/their value(s).
