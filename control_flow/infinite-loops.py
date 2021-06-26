# Infinite Loops

# lets edit the snippet from "while loops"
# we no longer need to define 'command' by setting
# it to an empty string. So the code becomes simpler

# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break

# EXERCISE

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")
