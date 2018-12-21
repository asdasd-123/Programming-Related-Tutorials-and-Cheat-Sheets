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

# Example 1 : Count() - Iterates up infinitely
for i in count(3):      # Will count up from 3 (inclusive)
    print(i)
    if i >= 11:         # until it hits 11
        break
