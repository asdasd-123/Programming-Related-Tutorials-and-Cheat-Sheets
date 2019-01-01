"""
==============================================================
Dunders
Dunders are special methods that have double underscores before and
after their names.
They're used to create functionality you cant get from normal methods.
For example, how to handle when two objects get added together
==============================================================
"""

# ==========
# One use of dunders is for "operator overloading".
# This allows us to use operators (+ and - etc) on the objects
# ==========
# For example, the __add__ dunder below allows us to add two vectors
# and return a third:
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)


# We can now create two vectors and add them together to get a third
vector_a = Vector(4, 5)
vector_b = Vector(2, 8)
vector_c = vector_a + vector_b  # becomes a vector with x=6 and y=13
print(str(vector_c))

# A list of common dunders is below:
# __sub__ for -
# __sub__ for -
# __mul__ for *
# __truediv__ for /
# __floordiv__ for //
# __mod__ for %
# __pow__ for **
# __and__ for &
# __xor__ for ^
# __or__ for |
