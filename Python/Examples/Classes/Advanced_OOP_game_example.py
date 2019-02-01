"""
==============================================================
A more in-depth game example showing how you can attack and kill the goblin
==============================================================
"""


class GameObject:
    """
    The class that all objects inherit from.
    """
    class_name = ""
    desc = ""
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.name] = self

    def get_desc(self):
        return self.class_name + ": " + self.name + "\n" + self.desc


class Goblin(GameObject):
    def __init__(self, name):
        self.class_name = "goblin"
        self.health = 3
        self._desc = "A foul creature"  # Notice the _ at the beginning
        super().__init__(name)  # Runs the GameObject.__init__,
        #                         which sets self.name = name
        #                         and adds goblin to the object list.

    @property   # Setting the below as a read-only attribute for description
    def desc(self):
        if self.health >= 3:
            return self._desc  # If uninjured return "a foul creature"
        elif self.health == 2:
            health_line = "It has a wound on its knee."
        elif self.health == 1:
            health_line = "Its left arm has been cut off!"
        elif self.health <= 0:
            health_line = "It is dead."
        return self._desc + "\n" + health_line
        # For example, if the goblin had 2hp. it would return:
        # >A foul creature
        # >It has a wound on its knee

    @desc.setter
    def desc(self, value):
        self._desc = value


# Input function to interpret list of commands
def get_input():
    input_text = input(": ")
    if input_text == "":
        print("Please enter a command")
        return
    command = input_text.split()
    verb_word = command[0]
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print(f'Unknown verb {verb_word}')
        return

    if len(command) >= 2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb("nothing"))


# Verb Functions
def say_function(noun):
    return f'You said {noun}'


def hit_function(noun):
    if noun in GameObject.objects:
        if GameObject.objects[noun].health <= 0:
            print("Stop hitting it, it's dead!")
            return
        else:
            GameObject.objects[noun].health -= 1
            return GameObject.objects[noun].desc
    else:
        return "You cant hit this"


verb_dict = {
    "say": say_function,
    "hit": hit_function
}


goblin1 = Goblin("Gobbly")
while True:
    get_input()


# Try typing "hit Gobbly" a few times to see what happens