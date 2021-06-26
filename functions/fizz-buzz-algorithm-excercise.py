# The Fizz Buzz Algorithm

# The Rules:
"""
1. If the number is divisible by 3,
    return 'Fizz'
2. If the number is divisible by 5,
    return 'Buzz'
3. If number is divisible by 3 AND 5,
    return 'Fizz Buzz'
4. If none are true,
    return back the given number.
"""

"""
# THIS WAS MY ATTEMPT. LOL. I TRIED.

def fizz_buzz(input):
    if input / 3 == 0:
        print("Fizz")
    elif input / 5 == 0:
        print("Buzz")
    elif input / 15 == 0:
        print("Fizz Buzz")
    else:
        return input


print(fizz_buzz(3))
"""

# Mosh's Solution:


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz(5))
