"""
Insance, Class, and Static methods
Following through the tutorial found here:
https://realpython.com/instance-class-and-static-methods-demystified/
"""


# ==========
# A simple class with all three method types.
# ==========
class MyClass:
    def mymethod(self):
        return "Instance method called", self

    @classmethod
    def myclassmethod(cls):
        return "Class method called", cls

    @staticmethod
    def mystaticmethod():
        return "Static method called"

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
