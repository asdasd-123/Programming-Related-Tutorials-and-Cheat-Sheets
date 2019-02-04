"""
==============================================================
More in-depth info on RegEx.
==============================================================
"""
import re

# ==========
# Metacharacters
# ==========
# These are what make RegEx more versatile than a simple string-replace tool.
# They function as concepts rather than literal characters.
# Such as "a number" rather than a specific number.
#
# Sometimes you need to search for a metacharacter like $ for example.
# To do this, escape them with \.
#
# Issues arise though due to \ being the normal escape character in
# strings already, which can lead to instances where you need
# 3 or 4 backslashes.
#
# To mitigate this issue, use raw strings can be used.

# All metecharacters:
# . ^ $ * + ? { [ ] \ | ( ) }

# ==========
# Metacharacter summary: (s for character)
# . ^ $ * + ? { [ ] \ | ( ) }
# ==========
# .s        - Any single character
# ^s        - Start of the string
# s$        - End of the string
# [s]       - Character classes
# [^s]      - Inverted character classes
# s*        - Zero or more repetitions of previous character
# [s]*      - Zero or more repetitions of previous class
# (s)*      - Zero or more repetitions of previous group

# ==========
# Metacharacter : . (any char)
# ==========
# Matches any single character. For example:
pattern = r"gr.y"

if re.search(pattern, "grey"):   # Will pass as a match
    print("Match 1")

if re.search(pattern, "gray"):   # Will pass as a match
    print("Match 2")

if re.search(pattern, "blue"):   # Will not pass as a match
    print("Match 3")

# ==========
# Metacharacter : ^ (start of string)
# ==========
# The start of a string. The following must occur directly at the
# start of the string.
pattern = r"^gr.y"

if re.search(pattern, "grey"):       # Will pass as a match
    print("Match 1")

if re.search(pattern, "grayabc"):    # Will pass as a match
    print("Match 2")

if re.search(pattern, "abcgray"):    # Will not pass as a match
    print("Match 3")

# ==========
# Metacharacter : $ (end of string)
# ==========
# The end of a string. The following must occur directly at the
# end of the string.
pattern = r"gr.y$"

if re.search(pattern, "grey"):       # Will pass as a match
    print("Match 1")

if re.search(pattern, "grayabc"):    # Will not pass as a match
    print("Match 2")

if re.search(pattern, "abcgrey"):    # Will pass as a match
    print("Match 3")

# You can combined the start^ and end$ characters as follows
# to make sure the pattern matches the whole string, not just part of it.
pattern = r'^gr.y$'

if re.search(pattern, "gray"):       # Will pass as a match
    print("Match 1")

if re.search(pattern, "grayabc"):    # Will not pass as a match
    print("Match 2")

if re.search(pattern, "abcgrey"):    # Will not pass as a match
    print("Match 3")

# ==========
# Metacharacters : [] (character classes)
# ==========
# Square brackets are used to dictate a set of characters that
# could match. Like a more restrictive version of the .(dot) character.
pattern = r"[aeiou]"    # This means that any single vowel
#                         will flag as a match.

if re.search(pattern, "grey"):      # Will pass as a match
    print("Match 1")

if re.search(pattern, "qwertyui"):  # Will pass as a match
    print("Match 2")

if re.search(pattern, "rhythm"):    # Will not pass as a match
    print("Match 3")

# Character classes can also include ranges using the - character.
pattern = r"[0-9][0-9]"     # This will only match a string with
#                             two consecutive numbers in it.

if re.search(pattern, "abs6jdf9"):  # Will not pass as a match
    print("Match 1")

if re.search(pattern, "abs45sks"):  # Will pass as a match
    print("Match 2")

# Ranges can be combined inside a single character class too.
pattern = r"[A-Za-z0-9]"    # will match any single letter or number
#                             regardless of case, but will not match
#                             any special characters.

if re.search(pattern, "s4F9k"):     # Will pass as a match
    print("Match 1")

if re.search(pattern, r"!£"):       # Will not pass as a match
    print("Match 2")

# ==========
# Metacharacters : [^] (inverted character classes)
# ==========
pattern = r"[^A-Z]"     # Will not match uppercase letters.

if re.search(pattern, "ABCD"):  # Will not pass as a match
    print("Match 1")

if re.search(pattern, "ab9d"):  # Will pass as a match
    print("Match 2")

# ==========
# Metacharacters : * (zero or more repetitions of previous thing)
# ==========
pattern = r'ac*'  # Will match any string with a, followed by zero or more c's

if re.search(pattern, "and"):   # Will pass as a match (a)
    print("Match 1")

if re.search(pattern, "acc"):   # Will pass as a match (acc)
    print("Match 2")

if re.search(pattern, "uek"):   # Will not pass as a match
