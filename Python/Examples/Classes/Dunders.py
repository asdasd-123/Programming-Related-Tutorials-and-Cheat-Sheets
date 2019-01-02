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

# A list of common operator dunders is below:
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

# __repr__ for string representation of the object. i.e print(Object)

# There are also magic-methods for comparisons.
# __lt__ for <
# __le__ for <=
# __eq__ for ==
# __ne__ for !=     # The 'r' method for this is __eq__
# __gt__ for >
# __ge__ for >=


# ==========
# 'r' methods
# These are used if a dunder cannot be found when checked.
# ==========
# i.e if object 'A' doesn't have a __add__ method, but object 'B' does has a
# __radd__ method.
# When we try A + B, it will search for A().__add__(B()) but it wont be found.
# At this stage it will try and find B().__radd__(A()) instead,
# which will work.
class NumberA:
    def __init__(self, x):
        self.x = x


class NumberB:
    def __init__(self, x):
        self.x = x

    def __radd__(self, other):  # If this was just __add__ it would't work.
        return NumberB(self.x + other.x)


a = NumberA(4)
b = NumberB(7)
c = a + b
print(c.x)  # prints out 11. It essentially calls B(7).__radd__(A(4())


# ==========
# Magic Methods for making classes act like containers
# ==========
# The common ones are:
# __len__ for len()
# __getitem__ for indexing
# __setitem__ for assigning to indexed values
# __delitem__ for deleting indexed values
# __iter__ for iteration over objects (e.g., in for loops)
# __contains__ for in
# For example, below:

class MyList:
    def __init__(self, cont):
        self.cont = cont

    def __getitem__(self, index):
        return self.cont[index]

    def __len__(self):
        return len(self.cont)


myList1 = MyList(['a', 'b', 'c', 'd'])
print(len(myList1))     # Prints 4
print(myList1[2])       # Prints 'c'
print(myList1[:2])      # Prints ['a', 'b']


# ==========
# Data hiding in classes
# Python has no way to make a variable private in a class,
# but it can mark them as not-intended to be changed externally.
# This is achieved by naming it with a single _ at the beginning.
# When a user imports it using "from abc import *", it will be ignored.
# ==========
class AObject:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "AObject({})".format(self._hiddenlist)


AObject = AObject([1, 2, 3])
print(AObject)              # Prints AObject([1, 2, 3])
AObject.push(0)
print(AObject)              # Prints AObject(0, 1, 2, 3)
AObject.pop()
print(AObject)              # Prints AObject(0, 1, 2)
print(AObject._hiddenlist)  # Prints [0, 1, 2]
