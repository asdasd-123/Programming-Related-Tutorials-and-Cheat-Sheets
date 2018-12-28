"""
==============================================================
Classes
Classes can contain both data and functionality together and
form the basis of OOP (Object Orientated Programming).
The example below follows through info found at:
http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html#classes-and-objects-the-basics
==============================================================
"""


# ==========
# Basic example of a class that takes no arguments
# ==========
class Point:
    """Point class represents and manipulates x,y coords."""

    def __init__(self):
        """Create a new point at the origin"""
        self.x = 0
        self.y = 0

p = Point()     # Instantiate an object of type Point
q = Point()     # Make a second point
print(p.x, p.y, q.x, q.y)   # Prints 0 0 0 0 - because the default values above

p.x = 3
p.y = 4
print(p.x, p.y, q.x, q.y)   # Prints 3 4 0 0

x = p.x
print(x)                    # Prints 3

# Dot notation works as part of any expression. Like below:
print("(x={0}, y={1})".format(p.x, p.y))    # prints (x=3, y=4)


# ==========
# A better example of a class that accepts arguments
# ==========
class PointV2:
    """Point class represents and manipulates x,y coords."""

    def __init__(self, x=0, y=0):
        """Create a new point at x,y"""
        self.x = x
        self.y = y

# Now we can create a point and set it's co-ords in a single line
p = PointV2(4, 2)
q = PointV2(6, 3)
r = PointV2()       # This defaults to 0,0 as we set it in the class
print(p.x, q.y, r.x)    # Prints 4, 3, 0


# ==========
# Adding methods to a class
# ==========
class PointV3:
    """Point class represents and manipulates x,y coords."""

    def __init__(self, x=0, y=0):
        """Create a new point at x,y"""
        self.x = x
        self.y = y

    def d_f_o(self):
        """Compute distance from origin"""
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def to_string(self):
        """Convert coords to string"""
        return "({0}, {1})".format(self.x, self.y)


p = PointV3(3, 4)
print("(x={0}, y={1}) Distance from origin is {2}".format(p.x, p.y, p.d_f_o()))
# Prints (x=3, y=4) Distance from origin is 5.0

q = PointV3(51, 8.5)
print("(x={0}, y={1}) Distance from origin is {2}".format(q.x, q.y, q.d_f_o()))
# Prints (x=51, y=8.5) Distance from origin is 51.70348...

print(p.to_string())    # Prints (3, 4)


# ==========
# Adding hanlders for conversion using str() for example
# ==========
class PointV4:
    """Point class represents and manipulates x,y coords."""

    def __init__(self, x=0, y=0):
        """Create a new point at x,y"""
        self.x = x
        self.y = y

    # By naming the method this, the str() will know how to convert
    def __str__(self):
        """Convert coords to string"""
        return "({0}, {1})".format(self.x, self.y)

    def d_f_o(self):
        """Compute distance from origin"""
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

p = PointV4(3, 4)
print(str(p))   # Now prints (3, 4)
