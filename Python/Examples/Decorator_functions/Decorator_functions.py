"""
==============================================================
Decorator Functions
==============================================================
"""


# Example 1:Using multiple decorators
def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap


def decor1(func):
    def wrap1():
        print("**************")
        func()
        print("**************")
    return wrap1


@decor
@decor1
def print_text():
    print("Hello world!")

print_text()


# The outcome:
# ===========
# **************
# Hello world!
# **************
# ===========
