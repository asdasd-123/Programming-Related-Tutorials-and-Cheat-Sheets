"""
==============================================================
Simple text-based game example showcasing how OOP (Object Orientated
Programming) is used.
Example taken from sololearn.
==============================================================
"""


def get_input():
    command = input(": ").split()
    verb_word = command[0]
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print(f"Unknown verb {verb_word}")
        return

    if len(command) >= 2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb("nothing"))


def say_function(noun):
    return f'You said {noun}'


def grab_function(noun):
    return f'You grab the {noun}'


verb_dict = {
    "say": say_function,
    "grab": grab_function
}

# ==========
# Walking through the program
# ==========

# verb_dict = {"say": say_function, "grab": grab_function}
# -----------
# This is a dictionary containing a list of verbs, and the function relating
# to each one.

# get_input()
# -----------
# This function is what is run on the game loop. I.e it will run over and over.

# command = input(": ").split()
# -----------
# This asks for a command and splits the words in it into a list.
# By leaving the split parameter blank, it uses space as the delimiter.
# i.e "Say Hello" becomes the list ['Say', 'Hello'].

# verb_word = command[0]
# -----------
# This takes the first word in our list above and stores it as the
# verb_word variable. In this case, "Say".

# if verb_word in verb_dict:
#     verb = verb_dict[verb_word]
# -----------
# This checks if the verb we just saved above exists in our dictionary.
# In this example, "Say" does appear in the dictionary.

# else:
#     print(f"Unknown verb {verb_word}")
#     return
# -----------
# If the verb is NOT found in the verb dictionary, it will tell the user and
# stop the function.

# if len(command) >= 2:
#     noun_word = command[1]
#     print(verb(noun_word))
# else:
#     print(verb("nothing"))
# -----------
# This section checks how many words we entered (from the command list we
# made before).
# If we entered more than 1, then it saves the 2nd word as "noun_word" then
# runs the function that related to the verb with the noun as the parameter.
# If we only entered one word, it will again run the verb function but only
# send "nothing" as the parameter

# def say_function(noun):
#     return f'You said "{noun}'
# -----------
# This is the function called when someone enters the verb "Say".

# def grab_function(noun):
#     return f'You grab the {noun}'
# -----------
# This is the function called when someone enters the verb "Grab".

# ==========
# Example inputs and results.
# ==========

# "Grab Spam"
# Prints out "You grabbed the Spam"

# "Grab"
# Prints out "You grabbed the nothing"

# "Say Hello"
# Prints out "You said Hello"

# "Say"
# Prints out "You say nothing"

"""
==============================================================
Now we introduce classes into it.
==============================================================
"""


class GameObject:
    class_name = ""
    desc = ""
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.class_name] = self

    def get_desc(self):
        return self.class_name + "\n" + self.desc


class Goblin(GameObject):
    class_name = "goblin"
    desc = "A foul creature"


def examine_function(noun):
    if noun in GameObject.objects:
        return GameObject.objects[noun].get_desc()
    else:
        return f"There is no {noun} here."


red_goblin = Goblin("Gobbly")

verb_dict = {
    "say": say_function,
    "grab": grab_function,
    "examine": examine_function
}

while True:
    get_input()

# ==========
# Walking through the next section
# ==========

# class GameObject:
#     class_name = ""
#     desc = ""
#     objects = {}
# -----------
# This creates a class called GameObject to handle all objects in the game.
# The class attributes have been set to two empty strings (placeholders) and
# an empty dictionary. The empty dictionary will be used to keep track of
# objects as they are created without needing to go back and manually
# add each one. Explained further below though.

# def __init__(self, name):
#         self.name = name
#         GameObject.objects[self.class_name] = self
# -----------
# When initialised, a name is supplied.
# It also adds a new entry into the objects dictionary with
# the key "self.class_name" and value "self".
# In this case since the key is blank still, nothing is added to the
# dictionary. This line is how objects will automatically be added later.

# def get_desc(self):
#         return self.class_name + "\n" + self.desc
# -----------
# This is a normal instance method that all sub classes will inherit.
# It just prints out the class name and the description. Currently both blank

# class Goblin(GameObject):
#     class_name = "goblin"
#     desc = "A foul creature"
#
# red_goblin = Goblin("Gobbly")
# -----------
# This is where we add a goblin class to the game and create one, which
# inherits from the GameObject class.
# When in initialises now, it sends the __init__ method above the two
# paramaters "Self", and "name". In this case "red_goblin" & "Gobbly".
# So the __init_ method now sets red_goblin.name(self.name) to "Gobbly"
# and does the following to add "Goblin" to the objects dictionary:
# (GameObject.objects[self.class_name]) = self
# which comes out as:
#  GameObject.objects[red_goblin.class_name] = "red_goblin"
# which equates to :
#  GameObject.objects["goblin"] = "red_goblin"

# def examine_function(noun):
#     if noun in GameObject.objects:
#         return GameObject.objects[noun].get_desc()
#     else:
#         return f"There is no {noun} here."
# -----------
# This is similar to the functions above for grab and say.
# It checks if the noun supplied is in the list of known game objects.
# If it is, it will send back the descriptiption of the game object.
# If not, it will send back "there is no noun here".

# ==========
# Example inputs and results.
# ==========

# "examine"
# Prints out "There is no nothing here"

# "examine goblin"
# Prints out:
# goblin
# A foul creature

# "examine chair"
# Prints out "There is no chair here"
