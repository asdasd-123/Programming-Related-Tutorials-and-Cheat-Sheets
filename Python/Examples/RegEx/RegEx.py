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
# Metacharacter summary:
# . ^ $ * + ? { [ ] \ | ( ) }
# ==========
# .     - Any single character

# ==========
# Metacharacter : . (dot)
# ==========
# Matches any single character. For example:
pattern = r"gr.y"

if re.match(pattern, "grey"):   # Will pass as a match
    print("Match 1")

if re.match(pattern, "gray"):   # Will pass as a match
    print("Match 2")

if re.match(pattern, "blue"):   # Will not pass as a match
    print("Match 3")
