"""
==============================================================
Itertools
The module itertools is a standard library that contains several functions
that are useful in functional programming.
One type of function it produces is infinite iterators.
The function count counts up infinitely from a value.
The function cycle infinitely iterates through an iterable
(for instance a list or string).
The function repeat repeats an object, either infinitely or
a specific number of times.
==============================================================
"""
from itertools import count     # needs importing first

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
