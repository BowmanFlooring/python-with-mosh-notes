# -------------------------------------------------------------------------------

# Performing Arithmetic Operators

# We can also implement certain magic methods for performing arithmetic opera-
# tions between two objects. Let's dive in:

# NOTE: THIS IS JUST ONE EXAMPLE. THERE ARE QUITE A FEW MORE THAN THIS.
# NOTE2: IN MOSH'S EXAMPLE, HE ONLY PRINTED 'combined.x' AT THE END - I CHOSE
# TO USE A FORMATTED STRING TO KEEP THE VISUAL 'COORDINATE' FORMAT.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(10, 20)
other = Point(1, 2)
combined = point + other
print(f"({combined.x}, {combined.y})")
