# ==============================================================
# Text analyser
# ==============================================================
from pathlib import Path
from os import getcwd
<<<<<<< HEAD
=======
print(getcwd())
>>>>>>> e5bcf17b1edd6591d8c773eb38c36fd3984c0729

filename = Path(getcwd() + "/Files/Test_file.txt")


def char_count(text, char):
    """
    Counts the number of times a specific character appears in a piece of text
    Returns the count as int
    """
    count = 0               # Start count at 0
    for v in text:          # loop through each character item in the text
        if v.upper() == char.upper():       # If character matches the one we're searching for
            count += 1      # Increase count by 1
    return count            # Return the final count after finishing the loop


with open(filename) as f:       # Open test text file
    text = f.read()             # save contents of file to "text"
<<<<<<< HEAD

for char in "abcdefghijklmnopqrstuvwxyz":
    print(len(text))
    print(char_count(text, char))

input('End')
=======

for char in "abcdefghijklmnopqrstuvwxyz":
    print(char + " - " + str(round((char_count(text, char) / float(len(text))) * 100)) + "%")
>>>>>>> e5bcf17b1edd6591d8c773eb38c36fd3984c0729
