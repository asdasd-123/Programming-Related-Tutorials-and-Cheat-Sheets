"""
==============================================================
Example of how to create, read, and set config files.
==============================================================
"""
import configparser

# ==========
# Writing to a config file
# ==========
# Before anything.
# Create a config object
config = configparser.ConfigParser()

# Set configeration of Default category all in one go
config['DEFAULT'] = {'serveraliveinterval': '45',
                     'compression': 'yes',
                     'compressionLevel': '9'}

# Or you can create a categiory before asigning values:
config['TEST2'] = {}
config['TEST2']['user'] = 'hg'

# Another method of setting valyes is as follows:
config['TEST3'] = {}
test_config = config['TEST3']
test_config['port'] = '50022'
test_config['forwardX11'] = 'yes'


# Now to write the current config.
with open('example.ini', 'w') as configfile:
    config.write(configfile)

# This saves the folowing file:
# IT SAVES ALL BUT CATEGORIES LOWERCASE
"""
[DEFAULT]
serveraliveinterval = 45
compression = yes
compressionlevel = 9

[TEST2]
user = hg

[TEST3]
port = 50022
forwardx11 = yes
"""

# ==========
# Reading from a config file
# ==========
# Before anything.
# Create a config object
config = configparser.ConfigParser()

print(config.sections())
# prints nothing because nothing has been loaded yet.

# Read the config file now
config.read('example.ini')

print(config.sections())
# Now prints ['TEST2', 'TEST3']. Notice DEFAULT is missing.


# ==========
# Using the info read from a config file
# (reading always returns a string so needs converting)
# ==========
# Can check if a category exists using the following
test = 'TEST2' in config
print(test)     # Prints True

test = 'asdfg' in config
print(test)     # Prints False

# An item can be read as follows (returns string)
test = config['TEST2']['user']
print(test)     # Prints hd

# ==========
# Using get() like with dictionaries.
# ==========
test_config = config['TEST3']
print(test_config.get('port'))  # Prints 50022

# By using this method, you can specify a fall-back value if it is not found.
# For example:
test_config.get('asdf')
# Would print nothing
# but
test_config.get('asdf', 'fallback-string')
# Would print the fallback-string

# NOTES :
# DEFAULT values have precedent over other categories.
# If you try to find a value that doesn't exist in the category
# your searching, but it does exist in the DEFAULT category,
# it will return the DEFAULT category value. Even if you supplied
# a fallback string.

# ==========
# Changing from string to other data types
# ==========
test = config['DEFAULT']['Compression']
print(test)     # Prints "yes"

test = config['DEFAULT'].getboolean('Compression')
print(test)     # Prints "True"

# Other commands include:
# .getint()
# .getfloat()
