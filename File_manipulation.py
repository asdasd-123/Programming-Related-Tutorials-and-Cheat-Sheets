# ==============================================================
# opening / closing Files
# ==============================================================

my_file = open("test.txt")         # opens the file in readonly mode
my_file = open("test.txt", "r")    # opens the file in readonly mode
my_file = open("test.txt", "w")    # opens the file in write mode (clears)
my_file = open("test.txt", "wb")   # opens the file in binary mode

# Other options include:

# Opens a file for both reading and writing.
# The file pointer placed at the beginning of the file.
my_file = open("test.txt", "r+")

# Opens a file for both writing and reading.
# Overwrites the existing file if the file exists.
# If the file does not exist, creates a new file for reading and writing.
my_file = open("test.txt", "w+")

# Opens a file for both appending and reading.
# The file pointer is at the end of the file if the file exists.
# The file opens in the append mode.
# If the file does not exist, it creates a new file for reading and writing.
my_file = open("test.txt", "a+")

my_file.close()     # Closes the file

# ==============================================================
# Reading from files
# ==============================================================

my_file = open("test.txt", "r")     # Opens file in read mode
cont = my_file.read()               # stores contents of my_file
print(cont)                         # prints contents to console
my_file.close()                     # closes file
