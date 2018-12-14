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
# Read entire contents:
my_file = open("test.txt", "r")     # Opens file in read mode
cont = my_file.read()               # stores contents of my_file
print(cont)                         # prints contents to console
my_file.close()                     # closes file

# Read contents by line, store as list:
file = open("filename.txt", "r")
print(file.readlines())             # includes the \n newline characters
file.close()

# can be condenses into single line like follows:
lines_in_file = len(open("test.txt").readlines())


# use for loop to read line by line instead:
file = open("test.txt", "r")
for line in file:
    print(line)                     # includes the \n newline characters
file.close()

# ==============================================================
# Writing to files
# ==============================================================

file = open("Test_files\\new_file.txt", "w")    # Opens file in write mode
file.write("This has been written to a file")   # Writes text to file
file.close()                                    # Closes file

# The write() method also returns the number of bytes written, for example:
msg = "Hello world!"
file = open("Test_files\\new_file.txt", "w")
amount_written = file.write(msg)
print(amount_written)                           # Would print 12
file.close()

# It is good practice to avoid wasting resources by making sure
# that files are always closed after they have been used.
# One way of doing this is to use try and finally, like below:
try:
    f = open("Test_files\\new_file.txt")
    print(f.read())
finally:
    f.close()
