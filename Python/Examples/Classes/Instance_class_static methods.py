"""
Insance, Class, and Static methods
Following through the tutorial found here:
https://realpython.com/instance-class-and-static-methods-demystified/
"""

import math


# ==========
# A simple class with all three method types.
# ==========
class MyClass:
    def mymethod(self):
        return "Instance method called", self   # Returns a tuple

    @classmethod
    def myclassmethod(cls):
        return "Class method called", cls   # Returns a tuple

    @staticmethod
    def mystaticmethod():
        return "Static method called"   # Returns a string

# Instance Method:
# The first one above is a normal 'instance' method.
# It takes one parameter (could take more) which points to an instance
# of MyClass.
# The 'self' parameter allows it free access to attributes and methods
# of the same object.
# They can also access the class itself through self.__class__ which means
# they can modify the class state.

# Class Method:
# The second one above is a 'class' method, indicated via the @classmethod
# decorator.
# This takes a 'cls' parameter instead of the 'self' one used before. (can
# still take others in addition).
# This points to the class, not the object instance when the method is called.
# Because it only has access to the cls/class, it loses the ability to
# modify the object instances state (which would require access to self).
# But by accessing the class directly, they can modify the class state and
# modify it across all instances of the class. i.e changing a class variable.

# Static Method:
# The third one above is a 'static' method, indicated via the @staticmethod
# decorator.
# This type of method doesn't take a 'self' or 'cls' paremeter (can still
# take others).
# This method cannot modify the class or object instance. They have restricted
# access to data, and normally used as a way to namespace methods.


# ==========
# Examples of calling them on an object
# ==========
obj = MyClass()

# Instance method
x = obj.mymethod()
print(x)
# Prints ('Instance method called', <__main__.MyClass object at 0x035F4690>)
# This also works the same as passing the object manually to a class as below:
x = MyClass.mymethod(obj)
print(x)

# Class method
x = obj.myclassmethod()
print(x)
# Prints ('Class method called', <class '__main__.MyClass'>)

# Static method
x = obj.mystaticmethod()
print(x)
# Prints Static method called


# ==========
# Examples of calling them directly on the class
# ==========

# Instance method
# x = MyClass.mymethod()
# print(x)
# This will fail with a TypeError. Python tried to populate the 'self'
# argument and failed since we haven't created the object.


# Class method
x = MyClass.myclassmethod()
print(x)
# Prints ('Class method called', <class '__main__.MyClass'>)
# This works since it doesn't require the 'self' argument and instead
# calls direcly on the class itself.

# Static method
x = MyClass.mystaticmethod()
print(x)
# Prints Static method called
# This works since it doesn't require the 'self' argument.


# ==========
# More real-use example
# ==========
# Example simple pizza class.
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'
        # Pizza(['cheese', 'tomatoes'])


print(Pizza(['cheese', 'tomatoes']))
# Prints "Pizza(['cheese', 'tomatoes']" due to the __repr__ method


# This new Pizza Class uses a classmethod to build a pizza
# with set a set ingredient list.
class PizzaV2:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'PizzaV2({self.ingredients!r})'

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])


pizza1 = PizzaV2.margherita()
# Genertates a PizzaV2 class with the ingredients already set
print(pizza1)
# Prints "PizzaV2(['mozzarella', 'tomatoes'])"

pizza2 = PizzaV2.prosciutto()
# Genertates a PizzaV2 class with the ingredients already set
print(pizza2)
# Prints "PizzaV2(['mozzarella', 'tomatoes', 'ham'])"


# ==========
# When to use static methods
# ==========
class PizzaV3:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'PizzaV3({self.radius}, '
                f'{self.ingredients})')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi


p = PizzaV3(4, ['mozzaella', 'tomatoes'])
print(p)
# Prints "PizzaV3(4, ['mozzaella', 'tomatoes'])"

print(f'{round(p.area(),2)} inch square')
# Prints "50.27 inch square"

# As nothing other than a radius needs to be supplied, it can be called
# directly from the class without creating an object first.
# For example:
print(PizzaV3.circle_area(4))
# Prints "50.26548245743669"

# ==========
# Final Takeaway points : 
# ==========

# Static and class methods are used to communicate the developers intent
# and to help avoid accidental mis-use of a method.

# Instance methods need a class instance (object) to have been created
# and access the instance through "self".

# Class methods dont need a class instance. they have access via "cls"

# Static methods dont have access through either cls or self, but work
# like regular functions.