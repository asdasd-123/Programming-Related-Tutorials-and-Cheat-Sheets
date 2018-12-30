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
# Adding handlers for conversion using str() for example
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


# ==========
# Using instances as return values
# ==========
class PointV5:
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
        return((self.x ** 2) + (self.y ** 2)) ** 0.5

    # In this example, a new point object can be returned
    def halfway(self, target):
        """Return the halfway point between itself and the target"""
        mx = (self.x + target.x) / 2.
        my = (self.y + target.y) / 2.
        return PointV5(mx, my)


# The below finds the halfway point between p and q
p = PointV5(3, 4)
q = PointV5(13, 8)
r = q.halfway(p)
print(str(r))       # Prints (8.0, 6.0)

# The below combines it all into one line.
print(str(PointV5(3, 4).halfway(PointV5(13, 8))))   # Prints (8.0, 6.0)


# ==========
# Setting Class attributes
# ==========
class Dog:
    """This is a dog"""
    legs = 4    # This attribute will be accessible without creating an object

    def __init__(self, name, colour):
        self.name = name
        self.colour = colour


fido = Dog("Fido", "brown")
print(fido.legs)    # Prints 4
print(Dog.legs)     # Prints 4


# ==========
# Inheritance
# ==========
class Animal:       # Set up the original 'super class'
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour


class Dog(Animal):      # By including "animal", it inherits all the
    def bark(self):     # animal info. This is a 'sub class'
        print("Woof!")


class Cat(Animal):
    def purr(self):
        print("Purr...")

fido = Dog("Fido", "brown")
print(fido.colour)
fido.bark()


# ==========
# Inheritance with overriding methods or attributes
# ==========
class Wolf:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def bark(self):
        print("Grr...")


class Dog(Wolf):
    def bark(self):     # This overrides the 'bark' method in Wolf
        print("Woof")

husky = Dog("Max", "grey")
wolf = Wolf("wolf", "grey")

husky.bark()
wolf.bark()


# ==========
# Inheritance can have multiple levels of inheritance
# ==========
class A:        # Class A can use method 1, but not method 2 or method 3
    def method1(self):
        print("Method 1")


class B(A):     # Class B can use method 1, method 2, but not method 3
    def method2(self):
        print("Method 2")


class C(B):     # Class C can use method 1, method 2, method 3
    def method3(self):
        print("Method 3")


# ==========
# Using the super function to access a 'super class' method
# Usful if a current sub-class method has overridden it
# ==========
class A:
    def spam(self):
        