#! python3
# -*- coding: utf-8 -*-
#title					:classDogBlueprint.py
#author					:Debashmita
#date of creation		:11/07/2022 14:34
#==============================================================================

class Dog:
    """ Blueprint of a dog """
    # class variable shared by all instances
    species = ["canis lupus"]
    
    def __init__(self, name, color):
        self.name = name
        self.state = "sleeping"
        self.color = color
    def command(self, x):
        if x == self.name:
            self.bark(2)
        elif x == "sit":
            self.state = "sit"
        else:
            self.state = "wag tail"
    def bark(self, freq):
        for i in range(freq):
            print("[" + self.name
            + "]: Woof!")

bello = Dog("bello", "black")
alice = Dog("alice", "white")
print(bello.color) # black
print(alice.color) # white
bello.bark(1) # [bello]: Woof!
alice.command("sit")
print("[alice]: " + alice.state)
# [alice]: sit
bello.command("no")
print("[bello]: " + bello.state)
# [bello]: wag tail
alice.command("alice")
# [alice]: Woof!
# [alice]: Woof!
bello.species += ["wulf"]
print(len(bello.species)
== len(alice.species)) # True (!)