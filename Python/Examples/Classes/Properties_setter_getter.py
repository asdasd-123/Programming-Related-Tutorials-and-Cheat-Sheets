"""
==============================================================
Setter/Getter Functions
Following on from the properties.py file, you can use setter/getter
functions to control the access (read and write) of the internal
property.
==============================================================
"""


# Example taken from comments on sololearn course. Following on from
# the pizza example in properties.py
class Pizza:
    def __init__(self, toppings):
        self.toppings = list(toppings)
        self._pineapple_allowed = False
        # Singe _ at the start to indicate that it is hidden / shouldn't
        # be edited

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):  # Name must match the property.
        if value:
            password = input("Enter the password: ")
            if password == "Sw0rdf1sh!":
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert! Intruder!")


pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)

# ==========
# Walking through the final lines 1 by 1 now.
# ==========
pizza = Pizza(["cheese", "tomato"])
# This line creates an object named pizza from the Pizza class
# and submits a list of toppings.
# Typing Print(pizza.toppings) would return the following:
# ["cheese", "tomato"]

print(pizza.pineapple_allowed)
# The @property decorator changes the method into a read-only attribute.
# In this case it just returns the variable _pinapple_allowed which is
# set to False in the Pizza initialisation.

pizza.pineapple_allowed = True
# When trying to SET a property, it looks for the decorator with the
# @property_name.setter tag. In this case @pinapple_allowed.setter
# and runs that method it is tagged to (must be same name as the property).
# In this case, that method asks for a password before it will change
# the property value from False to True

print(pizza.pineapple_allowed)
# Now that the hidden variable has been changed, the propery will return the
# new value, True.
