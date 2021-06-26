# Debugging

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
        return total  # This is purposely indented INCORRECTLY


print("Start")
print(multiply(1, 2, 3))
