# ==============================================================
# Text analyser
# ==============================================================
from pathlib import Path
from os import getcwd

filename = Path(getcwd() + "/Files/Test_file.txt")


def char_count(text, char):
    """
    Counts the number of times a specific character appears in a piece of text
    Returns the count as int
    """
    count = 0               # Start count at 0
    for v in text:          # loop through each character item in the text
        if v == char:       # If character matches the one we're searching for
            count += 1      # Increase count by 1
    return count            # Return the final count after finishing the loop


with open(filename) as f:       # Open test text file
    text = f.read()             # save contents of file to "text"

for char in "abcdefghijklmnopqrstuvwxyz":
    print(len(text))
    print(char_count(text, char))

input('End')
