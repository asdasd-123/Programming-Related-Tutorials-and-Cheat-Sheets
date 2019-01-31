"""
==============================================================
Properties
A property in a class is shown by adding the @property decorator.
It allows you to read a method like a variable/attribute, as
it allows you to call it without using brackets ().
A common use of it is to create read-only class attributes.
Example below from sololearn comments section, user 'Aries Duke'
==============================================================
"""


# ==========
# Example class WITHOUT the @property decorator
# ==========
# This is still technically read only, but you call the method like normal
class My_wallet:
    def my_money(self):
        return "£100"


abc = My_wallet()
balance = abc.my_money()    # You call the method with the ()
print(balance)
# Prints "£100"


# ==========
# Example class WITH the @property decorator
# ==========
# This is the best practice way to create a read-only attribute
class My_walletV2:
    @property
    def my_money(self):
        return "£100"


abc = My_walletV2()
balance = abc.my_money      # Here it is treated as if it were a class variable
print(balance)
# Prints "£100"
# Trying to set the valye of "abc.my_money" would raise an error since it is a
# method, not an actual variable.


# ==========
# Example of how to create a normal rewritable attribute
# ==========
class My_wallet_changeable:
    my_money = "£100"


abc = My_wallet_changeable()
balance = abc.my_money
print(balance)
# Prints "£100"
abc.my_money = "£50"
balance = abc.my_money
print(balance)
# Now prints "£50" because it is a real attribute
