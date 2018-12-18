# ====================================
# ====================================
# Python Lists and Dictionaries
# ====================================
# ====================================

# ============
# 11 : New Entries
# Adding items to dictionary
# ============
print('\n\n11 : New Entries\n\n')
menu = {}                           # Empty dictionary
menu['Chicken Alfredo'] = 14.50     # Adding new key-value pair
print(menu['Chicken Alfredo'])

# Your code here: Add some dish-price pairs to menu!

menu['Apple'] = 1           # Adds Apple to menu
menu['Orange'] = 0.75       # Adds Orange to menu
menu['Pear'] = 0.6          # Adds Pear to menu


print("There are " + str(len(menu)) + " items on the menu.")
print(menu)

# ============
# 12 : Changing Your Mind
# Deleting items from dictionary
# ============
print('\n\n12 : Changing Your Mind\n\n')
# key - animal_name : value - location
zoo_animals = {'Unicorn': 'Cotton Candy House',
               'Sloth': 'Rainforest Exhibit',
               'Bengal Tiger': 'Jungle House',
               'Atlantic Puffin': 'Arctic Exhibit',
               'Rockhopper Penguin': 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']

zoo_animals['Rockhopper Penguin'] = 'Test Exhibit'


print(zoo_animals)

# ============
# 13 : Remove a Few Things
# Removing items from strings
# ============
print('\n\n13 : Remove a Few Things\n\n')

backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove('dagger')
print(backpack)

# ============
# 14 : It's Dangerous to Go Alone! Take This
# Manipulating lists within dictionaries
# ============
print('\n\n14 : It\'s Dangerous to Go Alone! Take This\n\n')

# Assigned a new list to 'pouch' ke
inventory = {'gold': 500,
             'pouch': ['flint', 'twine', 'gemstone'],
             'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()

# Your code here

# Adding a key 'pocket' and assigning a list to it
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
# Sorting the list found under the key 'backpack'
inventory['backpack'].sort()
# Removing dagger from the dictionary list 'backpack'
inventory['backpack'].remove('dagger')
# Adding 50 to the total gold
inventory['gold'] += 50

# ====================================
# ====================================
# A Day at the Supermarket
# ====================================
# ====================================

# ============
# 1 : BeFOR We Begin
# Using for loop to traverse lists
# ============
print('\n\n1 : BeFOR We Begin\n\n')

names = ["Adam", "Alex", "Mariah", "Martine", "Columbus"]

for x in names:
    print(x)

# ============
# 2 : This is KEY!
# Using for loop to traverse dictionaries
# ============
print('\n\n2 : This is KEY!\n\n')

webster = {"Aardvark": "A star of a popular children's cartoon show.",
           "Baa": "The sound a goat makes.",
           "Carpet": "Goes on the floor.",
           "Dab": "A small amount."}

# Add your code below!
for definition in webster:
    # eg Aardvark - A star of a popular children's cartoon show.
    print(definition + ' - ' + webster[definition])

# ============
# 3 : Control Flow and Looping
# How to integtrate if statements into loops to control what we're looking for
# ============
print('\n\n3 : Control Flow and Looping\n\n')

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]  # Creates a list

for item in a:              # Loop through each number
    if item % 2 == 0:       # Check if number is even
        print(item)         # If number is even, print number

input()
