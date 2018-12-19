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
str = "Test String"

str.lower()             # Converts to lowercase - "test string"
str.upper()             # Converts to uppercase - "TEST STRING"
len(str)                # Returns length of string - 11
str.isalpha()           # Only letters? - False (space not a letter)
str[0]                  # Return first character - "T"
str[1:3]                # Return 2nd to 3rd (4th - 1) character - "es"
str[3:]                 # Return 4th to end characters - "t String"
# The following allows numbers to be put into a string without converting first
# using {} around the inputs
msg = "Numbers: {0} {1} {2}".format(4, 5, 6.5)
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

xDict['Key1']           # returns the item in Key1 - 1
xDict['KeyN'] = 'temp'  # Appends a new key with value 'temp'
del xDict['KeyN']       # Deletes 'KeyN' from the Dictionary

# For checking if a key is in a dictionary, use 'in' or 'not in'
# For example:
print('Key1' in xDict)      # Prints True
print('abc' not in xDict)   # Prints True
print('Key3' not in xDict)  # Prints False

# Can also use 'get' to return a set value if not found (default 'none')
print(xDict.get('key6', "not found"))    # Prints 'not found'

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
nums = [11, 22, 33, 44, 55]


# Map Example :
# Setup a function. This one adds 5 to whatever it's sent
def add_five(x):
    return x + 5

# The code below will go through every item in nums and run
# the add 5 function on it.
# when combined with list() it will return the following list back:
# 16,27,38,49,60
result = list(map(add_five, nums))
result = list(map(lamdbda x: x+5, nums))    # This does the same but in 1 line

print(result)   # Prints a list of 16,27,38,49,60


# Filter Example:
# The code below will loop through nums and only select items that are even
result = list(filter(lambda x: x % 2 == 0, nums))

print(result)   # Would print 22,44

# ==============================================================
# Exception Handling
# ==============================================================
# If your trying to track down a bug, you can use try/except/finally.
# Don't use except without a specific error. Bad practice.
# Can add multiple except blocks like 'elif'.
# can include multiple error types in one except with commas.
# ==============================================================

try:                                # Will try the code block below
    y = 5 / 0                       # This bit failes (divide by zero)
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


input("Question here")      # console input
