"""
==============================================================
Itertools
The module itertools is a standard library that contains several functions
that are useful in functional programming.
One type of function it produces is infinite iterators.
- The function "count" counts up infinitely from a value.
- The function "cycle" infinitely iterates through an iterable
  (for instance a list or string).
- The function "repeat" repeats an object, either infinitely or
  a specific number of times.
- Takewhile - takes items from an iterable while a predicate function
  remains true.
- Chain - combines several iterables into one long one.
- Accumulate - returns a running total of values in an iterable.
- Product - returns all combinations of two/more lists.
  Optional parameter "repeat=2" for example to use one list and treat it
  the same as two identical lists.
- Permutations - returns all possible combinations from a single list
==============================================================
"""
from itertools import count, repeat, cycle     # needs importing first
from itertools import takewhile, accumulate, chain
from itertools import product, permutations

# ==============================================================
# Count()
# ==============================================================

# Example 1 : Count(x) - Iterates up infinitely from x
for i in count(3):      # Will count up from 3 (inclusive)
    print(i)
    if i >= 11:         # until it hits 11
        break
# Prints 3,4,5,6,7,8,9,10,11

# Example 2 : count(x,y) - Iterates up infinitely from x in y increments
for i in count(3, 5):
    print(i)
    if i >= 42:
        break
# Prints 3,8,13,18,23,28,33,38,43

# Example 3 : count(x,-y) - Iterates down infinitely from x in y increments
for i in count(40, -8):
    print(i)
    if i <= 12:
        break
# Prints 40,32,24,16,8

# ==============================================================
# repeat()
# ==============================================================

# Example 1 : Repeat(x,y)
print(list(repeat("Spam", 10)))
# Prints a list of "Spam", 10 times

# ==============================================================
# cycle()
# ==============================================================

# Example 1 : Difference between cycle and normal for loop
# For loop:
for i in "Spam":
    print(i)
# Prints S,p,a,m

# commented the below as it's an infinite loop
# for i in cycle("Spam"):
#     print(i)
# Prints S,p,a,m,S,p,a,m,S,p,a,m.....

# ==============================================================
# accumulate()
# ==============================================================

# Example 1 : Make a list using accumulate and range
nums = list(accumulate(range(8)))
# Produces list 0,1,3,6,10,16,21,28
# (0),(0 + 1), (0 + 1 + 2) etc

# ==============================================================
# takewhile()
# ==============================================================

# Example 1 : Using Lambda + takewhile to return items in list until
# the rule is broken.
nums = [0, 2, 4, 6, 8, 10, 2, 3, 4, 5]
print(list(takewhile(lambda x: x <= 6, nums)))
# prints out 0,2,4,6 (ignores the items at the end because the rule
# failed on '8')

# ==============================================================
# chain()
# ==============================================================

# Example 1 : Using chain to join two lists
list(chain([1, 3, 2], [3, 5, 9]))
# produces a single list of 1,3,2,3,5,9

# ==============================================================
# product()
# ==============================================================

# With product, [1,2] is treated the same as [2,1]
product('ABCD', 'xy')               # Ax Ay Bx By Cx Cy Dx Dy
print(list(product(range(2), repeat=3)))  # 000 001 010 011 100 101 110 111
print(list(product(range(2), repeat=2)))  # 00 01 11 10

# ==============================================================
# permutations()
# ==============================================================

# Not that "a,b,c" is treated differently than "c,b,a" etc
print(list(permutations('abc')))
# "a,b,c" "a,c,b" "b,a,c" "b,c,a" "c,a,b" "c,b,a"
