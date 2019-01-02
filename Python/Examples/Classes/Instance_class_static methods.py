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
