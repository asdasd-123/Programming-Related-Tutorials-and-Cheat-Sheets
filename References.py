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
# ==============================================================
empty_list = []                             # A list can be initialised empty
xlist = ['a', 'b', 'c', 'e', 'd', 'f', 'f']     # or with data already in it.

xlist[1:3]              # Return 2nd to 3rd (4th - 1) character - "b,c"
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
xlist *= 3              # Muliplies the list the same as a string
new_list = list(range(10))  # Range can be used to populate a list, but
#                             needs converting with list(). This one creates
#                             a list with all inegers from 0-9
new_list = list(range(3, 8))    # Creates list of 3,4,5,6,7 (not 8)

# ==============================================================
# Dictionaries
# ==============================================================
xDict = {'Key1': 1, 'Key2': 2, 'Key3': 3, 'Key4': 4, 'Key5': 5}

xDict['Key1']           # returns the item in Key1 - 1
xDict['KeyN'] = 'temp'  # Appends a new key with value 'temp'
del xDict['KeyN']       # Deletes 'KeyN' from the Dictionary

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
# Exception Handling
# ==============================================================
# If your trying to track down a bug, you can use try/except.
# Don't use except without a specific error. Bad practice.
# Can add multiple except blocks like 'elif'.
# can include multiple error types in one except with commas.
# ==============================================================

try:                                # Will try the code block below
    y = 5 / 0                       # This bit failes (divide by zero)
except ZeroDivisionError:           # If error found above, run this code block
    print("there was an error!")

#
input("Question here")      # console input
