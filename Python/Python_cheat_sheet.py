import re
"""
My python cheat sheet.
More in-depth explanation on almost everything at here though:
https://gto76.github.io/python-cheatsheet/

Loads of useful modules here:
https://github.com/vinta/awesome-python
"""

# ==============================================================
# Docstrings
# ==============================================================
"""
Doc strings are a multi line comment used at the very start
of a function to explain it's purpose
It can be accessed and printed through
    function.__doc__
"""

# ==============================================================
# Variable Types
# ==============================================================
x = 10                          # Integer
x = 10.                         # Float
x = "10"                        # String
xlist = [2, '1', 2.2]           # List
xDict = {'key1': 1, 'Key2': 2}  # Dictionary

# Different Array types (all explained better below)
# list: [v], mutable, indexed
# tuple: (v), immutable, indexed
# dic: {k:v}, mutable, key:value pairs, no index
# set: {v}, mutable, unique elements, no index

# ==============================================================
#  Type Conversion
# ==============================================================
str(5)          # '5'   - Converts to string
int('5')        # 5     - Converts to integer
float('5')      # 5.0   - Converts to float (accepts string or int)

# ==============================================================
#  Misc
# ==============================================================
(8 + 4) / 2     # Produces 6.0 NOT 6 - Single / outputs float

20 // 3         # Produces 6 - (Quotient)
20 % 3          # Produces 2 - (Remainder)

'xyz' + 'abc'   # Produces 'xyzabc' (concatenation)

'2' + '2'       # '22'
2 + 2           # 4
# 2 + '2'       # ERROR

'a' * 6         # 'aaaaaa' - Only integer, not float
'a' * 0         # '' - blank string, but still valid

# ==============================================================
# In-Place Operators
# ==============================================================
# example variables
x = 4
y = 'spam'
# Instead of things like this :
x = x + 4               # 8
x = x - 4               # 0
x = x * 3               # 12
y = y + 'eggs'          # 'spameggs'
# Use this instead :
x += 4                  # 8 - same as x = x + 4
x -= 4                  # 0 - same as x = x - 4
x *= 3                  # 12 - Same as x = x * 3
y += 'eggs'             # 'spameggs' - same as y = y + 'eggs'

# ==============================================================
# Strings
# ==============================================================
string = "Test String"

string.lower()             # Converts to lowercase - "test string"
string.upper()             # Converts to uppercase - "TEST STRING"
len(string)                # Returns length of string - 11
string.isalpha()           # Only letters? - False (space not a letter)
string[0]                  # Return first character - "T"
string[1:3]                # Return 2nd to 3rd (4th - 1) character - "es"
string[3:]                 # Return 4th to end characters - "t String"
r"Test String"          # The r indicates a 'Raw string'.
#                         Raw strings ignore escape chars.
#                         so \n would be printed etc
# The following allows numbers to be put into a string without converting first
# using {} around the inputs
msg = "Numbers: {0} {1} {2}".format(4, 5, 6.5)
print(msg)
# This is also a shorter way of doing it
x = 5
y = 4
msg = f"These are my formatted numbers, {x}, {y}"
print(msg)

print("{0}{1}{0}".format("abra", "cad"))    # prints abracadabra for example
a = "{x}, {y}".format(x=5, y=12)            # Can also use named arguments

# Useful string functions:
# Join : joins a list of strings with another string as a separator
print(", ".join(["spam", "eggs", "ham"]))
# prints "spam, eggs, ham"

# Split - split is the opposite of join, turning a string with
# a certain separator into a list.
print("spam, eggs, ham".split(", "))
# prints "['spam', 'eggs', 'ham']"

# Replace - replaces one substring in a string with another
print("Hello ME".replace("ME", "world"))
# prints "Hello world"

# Startswith/Endswith - determine if there is a substring
# at the start and end of a string respectively
print("This is a sentence.".startswith("This"))
# prints "True"
print("This is a sentence.".endswith("sentence."))
# prints "True"

# ==============================================================
# range()
# ==============================================================
# range() can be used to produce varying lists of numbers quickly
# ==============================================================
# Formats include:
# range(end value)  -   Produces a list of all numbers from 0 to (end-1)
range(5)            # produces 0,1,2,3,4
# range(Start, End) -   Produces a list of all numbers from start to (end-1)
range(3, 9)         # prodeces 3,4,5,6,7,8
# range(Start, End, Interval) -   list from start to (end-1) at interavals
range(3, 20, 2)     # produces 3,5,7,9,11,13,15,17,19

# ==============================================================
# Lists
# ==============================================================
# Lists can be placed inside other lists
# References start at 0!
# ==============================================================
empty_list = []                             # A list can be initialised empty
xlist = ['a', 'b', 'c', 'e', 'd', 'f', 'f']     # or with data already in it.

xlist[1:3]              # Return 1st to 2nd (3rd - 1) character - "b,c"
xlist[1:6:3]            # Returns 1st through 5th character at 3 steps - 'b,d'
xlist[:-3]              # Negative values count back from the end - 'a,b,c,e'
xlist[-3:-1]            # 'e,d,f'
xlist[::-1]     # shortcut to reverse a list. (Full list stepping backwards)
xlist.append("g")       # Adds "g" to the end of the list
xlist.index('d')        # Gets index value of 'd'. in this case, 4 (start at 0)
xlist.sort()            # Sorts the list
xlist.count('f')        # Counts number of times item appears in list - 2
xlist.insert(3, 'c.5')  # Inserts 'c.5' after c, the 4th item (start at 0)
xlist.remove('b')       # Removes the first occurance of 'b'
xlist.reverse()         # Reverses the order of a list
max(xlist)              # returns the max item in the list (g in this case)
min(xlist)              # returns the min item in the list (a in this case)
xlist.clear()           # Empties the entire List
xlist += ['h', 'i', 'j']    # Adds the new list to the end of the current
xlist *= 3                  # Muliplies the list the same as a string
xlist[2] = 'c'              # Sets item 2 in the list to 'c'
new_list = list(range(10))  # Range can be used to populate a list, but
#                             needs converting with list(). This one creates
#                             a list with all inegers from 0-9
new_list = list(range(3, 8))    # Creates list of 3,4,5,6,7 (not 8)
cubes = [i**3 for i in range(5)]    # for loops can also be used

# If statements can also be bundled in too as below:
evens = [i**2 for i in range(10) if i**2 % 2 == 0]
# returns 0,4,16,36,64

# ==============================================================
# Tuples
# ==============================================================
# Tuples are more efficient lists buts contents cannot be changed
# 'Immutable'
# ==============================================================
xTuple = ('a', 'b', 'c', 'd')   # similar to list but with (), not []
xTuple2 = 'a', 'b', 'c'         # Also valid without any brackets
# xTuple[2] = 'c'   Would generate an error

# Tuples can also be "packed" and "unpacked" which can be useful
# for creating variables. i.eval
fruits = ("Apple", "Pear", "Banana")
f1, f2, f3 = fruits

print(f1)   # prints "Apple"
print(f2)   # prints "Pear"
print(f3)   # prints "Banana"

# ==============================================================
# Dictionaries
# ==============================================================
xDict = {'Key1': 1, 'Key2': 2, 'Key3': 3, 'Key4': 4, 'Key5': 5}
yDict = {}              # Creates an empty dictionary

xDict['Key1']           # Returns the item in Key1 - 1
xDict['KeyN'] = 'temp'  # Appends a new key with value 'temp'
del xDict['KeyN']       # Deletes 'KeyN' from the Dictionary

# For checking if a key is in a dictionary, use 'in' or 'not in'
# For example:
print('Key1' in xDict)      # Prints True
print('abc' not in xDict)   # Prints True
print('Key3' not in xDict)  # Prints False

# Can also use 'get' to return a set value if not found (default 'none')
print(xDict.get('key6', "not found"))    # Prints 'not found'

# You can combine dictionaries using the below example
aDict = {'a': 1, 'b': 2}
bDict = {'b': 3, 'c': 4}

cDict = {**aDict, **bDict}
print(cDict)    # prints {'a': 1, 'b': 3, 'c': 4}.
# Notice b is overwritten by the 2nd dictionary

# ==============================================================
# Sets
# ==============================================================
# Sets are similar to lists except they:
# - Only contain unique entries (duplicate items ignored)
# - Are not indexed
# - Iterating through them will happen in an unpredictable order
# - Use less memory
# - Faster to check if items are in it than lists
# ==============================================================
# Can be created the two ways below
set1 = {1, 2, 3, 4}
set2 = set()        # Cant use just {} as thats how dictionaries are made
set3 = {1, 2, 3, 3, 2, 1, 2, 3}     # Would just produce {1, 2, 3}
# Can use 'in' / 'not in' to check if items are in it
print(4 in set1)        # Prints True
print(3 not in set1)    # Prints False

# Can still use len() the same way as lists though
print(len(set1))        # Prints 4
print(len(set3))        # Prints 3 (no duplicates)

# But use 'add()' instead of 'append' to add items.
set1.add(5)

# And remove an item using remove()
# But using pop() will remove a random item since the list is unordered
set1.remove(5)

# Multiple sets can be combined in different ways. Shown below.
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)   # Union- Combine Sets - {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(first & second)   # Intersection- Only get items from both - {4, 5, 6}
print(first - second)   # Difference- Items in first but not second - {1, 2, 3}
print(second - first)   # Difference- Items in second but not first - {8, 9, 7}
print(first ^ second)   # symmetric difference- Items in either set but
#                         not both - {1, 2, 3, 7, 8, 9}

# ==============================================================
# If Statements
# ==============================================================
# Example use case is "If number is less than 5, do this. If not, do this".
# Use "elif" to chain together multiple if checks.
# Remember to indent either 2 or 4 spaces after an if statement for
# the code you want to run when true.
# ==============================================================
x = 5                           # First make a variable to check
templist = ['a', 'b', 'c']

if x < 0:                       # Check if x is less than 0 (dont forget the :)
    print('x is less than 0')   # If true, print the message
elif x >= 0:                    # Check if x is more than 0
    print('x is greater than 0')    # If true, print the message
else:                           # Only runs if all the if's above are false
    print('x must be 0')

# List of comparitors you can use in an if statement:
#   x < y   Less than
#   x <= y  Less than or equal to
#   x > y   Greater than
#   x >= y  Greater than or equal to
#   x == y  Equal to (always use two equals signs when comparing items)
#   x != y  Not equal to
#   's' in 'string' = True      Checks if 's' is in the string 'string' (True)
#   'd' in 'string' = False     Checks if 'd' is in the string 'string' (False)
#   'b' in templist = True      Checks if 'b' is in the list templist (True)
#   'd' in templist - False     Checks if 'd' is in the list templist (False)
#   x and y BOTH must be TRUE
#   x or y  ONE must be TRUE at least
#   using 'not' flips a TRUE or FALSE or can be combined with in.
#   i.e not TRUE equals FALSE       -   's' not in 'test' = False

# Example using all of the above that will be true and print out the message:
x = 5

if (not(x < 7) or (True and not(x != 5))):
    print('This is true')
else:
    print('if the above statement is false, this message will appear')

# Any/All can be used to check if all or some items in a for loop return True
nums = [55, 44, 33, 22, 11]
if all([i > 5 for i in nums]):          # Returns True
    print("All larger than 5")

if any([i % 2 == 0 for i in nums]):     # Returns True
    print("At least one is even")

# ==============================================================
# While Loops
# ==============================================================
# Will keep looping through a section of code until the check fails
# Warning: Can get stuck in infinite loop if the check never fails
# use the "break" command to exit a loop at any time.
# use the "continue" command to jump back to top of loop at any time
# ==============================================================
i = 1               # Set variable 'i' to 1
while i <= 5:       # Repeat the following while i is <= to 5
    print(i)        # Print the current value of i
    i += 1          # Add 1 to i. After this line, the loop repeats because
#                     i is still <= 5
print('finished!')  # When i is no longer <= 5, print out 'finished'

# ==============================================================
# For Loops
# ==============================================================
# Often used for looping through lists as it's much easier
# than using a while loop.
# The example below will loop through the whole list and print each item
temp_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]     # Setup a test list
for item in temp_list:
    print(item)

# can also use for loops to loop something for a set amount of times
for item in range(5):
    print('spam')       # This is print 'spam' 5 times

# Enumerate can be used to iterate through values AND indices
# of a list simultaneously. Useful when convertig lists to Dictionaries
nums = [55, 44, 33, 22, 11]
dict = {}
for v in enumerate(nums):
    key = v[0]
    dict[key] = v[1]
print("dict:")
print(dict)

# ==============================================================
# Functions
# ==============================================================
# Functions aren't used until they are 'called'.
# In this section, we first create a function,
# But dont call it until later
# Ignore contents of the function, 'for loops' explained later.
# ==============================================================


def count_small(numbers):       # First setup a function, with input "numbers"
    total = 0                   # In this case, numbers is a list.
    for n in numbers:           # REQUIRES 2 BLANK LINES
        if n < 10:              # BEFORE AND AFTER FUNCTION BLOCK.
            total = total + 1
    return total


lotto = [4, 8, 15, 16, 23, 42]  # Create a list called lotto
small = count_small(lotto)      # Call our function above and send it
#                                 the list called lotto.
#                                 It will then go through the function above,
#                                 return back the answer, and store as 'small'

print(small)                    # Prints the answer to the screen

# ==============================================================
# Lambda functions
# ==============================================================
# Lambda functions aren't as powerful as named functions.
# They can only do things that require a single expression,
# usually equivalent to a single line of code.
#
# Only really useful for map/filter function. Even then,
# simpler, more elegant solutions are usually available.
# ==============================================================


# Example named function
def polynomial(x):
    return x**2 + 5*x + 4


print(polynomial(-4))                   # prints out 0 (16-20+4)

# lambda function for same thing.
print((lambda x: x**2 + 5*x + 4)(-4))   # prints out 0 (16-20+4)


# Example below of Map usecase (Max explanation in next section)
def add_five(x):
    return x + 5


nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))  # returns a list of 16,27,38,49,60
print(result)

# Example of shorter map use with lambda instead (no need to define add_five)
result = list(map(lambda x: x+5, nums))

# Although with this example, it would be much better to just use this
result = [x + 5 for x in nums]

# ==============================================================
# Map / Filter
# ==============================================================
# Map: Used to apply a function to every item in a list.
# Must use list() to convert output from map object to list though.
#
# Filter: Used to apply a filter to a list.
# Must also use list() to convert the output.
# ==============================================================
# This is the list we'll be iterating through in the examples below
nums2 = [11, 22, 33, 44, 55]


# Map Example :
# Setup a function. This one adds 5 to whatever it's sent
def add_five2(x):
    return x + 5


# The code below will go through every item in nums and run
# the add 5 function on it.
# when combined with list() it will return the following list back:
# 16,27,38,49,60
result = list(map(add_five2, nums2))
result = list(map(lambda x: x+5, nums2))    # This does the same but in 1 line

print(result)   # Prints a list of 16,27,38,49,60


# Filter Example:
# The code below will loop through nums and only select items that are even
result = list(filter(lambda x: x % 2 == 0, nums))

print(result)   # Would print 22,44

# ==============================================================
# Generators
# ==============================================================
# Generators are a type of iterable, like lists or tuples.
# Unlike lists, they don't allow indexing with arbitrary indices,
# but they can still be iterated through with for loops.
# They can be created using functions and the yield statement.
# Much more memory efficient than large lists. Can be infinite
# ==============================================================


def countdown():
    i = 5
    while i > 0:
        yield i
        i -= 1


# Will loop through countdown() until it hits return or the end of function
for i in countdown():
    print(i)

# Generators can be used to create a list like the below:
nums = list(countdown())    # Creates the list [5,4,3,2,1]

# ==============================================================
# Decorator functions
# Allows creation of "add-on" functions and rename them.
# Allows you to create variations of a single function without copying
# 80% of the code.
# More examples of multiple decorators in Decorator_functions.py example file
# ==============================================================


# Example 1
def decor(func):            # Define the add-on function
    def wrap(x):        # define sub-function which will contain the decoration
        print("============")
        func(x)             # The function we will be parsing it (print_text)
        print("============")
    return wrap


def print_text(name):           # Define original function
    print("Hello:", name)


decorated = decor(print_text)   # Rename the function combination
decorated("Williams")           # Now it runs the first then second function
# prints the following:
# ============
# Hello: Williams
# ============


# Example 2
def decor2(func):               # Define the add-on function
    def wrap():        # define sub-function which will contain the decoration
        print("============")
        func()             # The function we will be parsing it (print_text)
        print("============")
    return wrap


@decor2                         # with the @ symbol you can decorate it
def print_text2():              # automatically but you lose ability to
    print("Hello world!")       # call it without the decorator.


print_text2()
# prints the following:
# ============
# Hellow World!
# ============

# ==============================================================
# Exception Handling
# ==============================================================
# If your trying to track down a bug, you can use try/except/finally.
# Don't use except without a specific error. Bad practice.
# Can add multiple except blocks like 'elif'.
# can include multiple error types in one except with commas.
# ==============================================================

try:                                # Will try the code block below
    y = 5 / 2               # If this was zero, it would fail (divice by zero)
except ZeroDivisionError:           # If error found above, run this code block
    print("there was an error!")
    raise                           # displays the original error
finally:                            # not used as much, but will run regardless
    print("This code will run no matter what")

# You can manually raise exceptions by using:
#   raise ZeroDivisionError
#   or
#   raise ZeroDivisionError("don't divide by zero!")
#

# ==============================================================
# Assertions
# ==============================================================
# Used to make sure something is "True"
# if it succeeds, the code continues
# If it fails, it throws an Assertation error

assert 5 == (2 + 3)     # The code will carry on running because this is True
# assert 5 == 1           This would raise an error becuase it returns False
assert 5 == 5, "If the assertain fails, this text is displayed"

# ==============================================================
# Recursion
# ==============================================================
# A function can be called from within itself. This leads to recursion
# They require a "Base Case". A way for the function to eventually end.
# More examples in the "itertools.py" example file
# ==============================================================
# The example below shows how to work out 6! (6 factorial)
# i.e 6 * 5 * 4 * 3 * 2 * 1         (720)


def factorial(x):
    if x == 1:              # This is needed to stop it from recurring forever
        return 1            # Called the "Base Case"
    else:
        return x * factorial(x-1)       # calls itself.


print(factorial(6))     # prints 720


# ==============================================================
# Classes
# ==============================================================
# Full in-depth breakdown found here:
# http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html#classes-and-objects-the-basics
# Examples that follow along with that link in the "Classes.py"
# example folder.
# More breakdown on 'self' variable here:
# https://pythontips.com/2013/08/07/the-self-variable-in-python-explained/
# ==============================================================
# Example class setup below
class PointV3:
    """Point class represents and manipulates x,y coords."""

    def __init__(self, x=0, y=0):
        """Create a new point at x,y"""
        self.x = x
        self.y = y

    def d_f_o(self):
        """Compute distance from origin"""
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5


p = PointV3(3, 4)
print("(x={0}, y={1}) Distance from origin is {2}".format(p.x, p.y, p.d_f_o()))
# Prints (x=3, y=4) Distance from origin is 5.0

# ==============================================================
# Regular Expressions
# ==============================================================
# Regular expressions (RegEx) are tools for string manipulation.
# Nearly all popular programming lanugages have a RegEx library due
# to how useful they can be.
# RegEx is essentially a pattern-recognition tool.
# The two main functions are:
# - Confirm that a string matches the set pattern
# - Replace pieces of a string that match the pattern
# More in-depth breakdown on pattern characters in "Examples/RegEx/RegEx.py"
# ====================s==========================================

# To use RegEx, you need to import it using:
# import re

# ============
# re.match(pattern, string)
# re.match checks if a pattern matches the START of a string.
# (case sensitive)
# ============
# pattern here is a simple string, but it can be a set of instructions
# i.e 2 numbers followed by 3 letters
pattern = r"spam"

if re.match(pattern, "spamspamspamspam"):
    print("Match!")
else:
    print("No Match!")
# Prints "Match!"

# ============
# re.search(pattern, string)
# Searches for a pattern ANYWHERE in a string.
# ============
pattern = r"spam"

if re.match(pattern, "eggspamsausagespam"):
    print("Match!")
else:
    print("No Match!")
# Prints "Match!"

# ============
# re.findall(pattern, string)
# Returns a list of all substrings that match the pattern.
# ============
pattern = r"spam"

print(re.findall(pattern, "eggspamsausagespam"))
# Prints ['spam', 'spam']

# Can be combined with len() to find out how many instances were found
print(len(re.findall(pattern, "eggspamsausagespam")))
# Prints 2

# ============
# re.finditer(pattern, string)
# Like findall but returns an iterable of all instances of the pattern found.
# ============
pattern = r"spam"

# Comments below are for the first insance it finds.
for x in re.finditer(pattern, "eggspamsausagespam"):
    print(x)            # Prints "<re.Match object; span=(3, 7), match='spam'>"
    print(x.group())    # String - Prints "spam"
    print(x.start())    # Int - Prints "3"
    print(x.end())      # Int - Prints "7"
    print(x.span())     # A tuple - Prints (3, 7)

# ============
# re.sub(pattern, repl, string, count=0, flags=0)
# Subsitutes "max" instances of a pattern with a new string.
# If max is left blank, then it replaces all instances.
# ============
input_str = r"Test String : abc / Test String : abc"
pattern = r"abc"

# Example WITHOUT a count being supplied
new_str = re.sub(pattern, "def", input_str)
print(new_str)
# Prints "Test String : def / Test String : def"

# Example WITH a count being supplied (only 1st is changed)
new_str = re.sub(pattern, "def", input_str, 1)
print(new_str)
# Prints "Test String : def / Test String : abc"

# input("Question here")      # console input
