# powerups.py

'''
title: Powerups Sprite
'''

from loader import *
from random import randrange
from box import Box

class Powerups(Box): # Concrete child class (inheriting from class Box)
    def __init__(self, window):
        Box.__init__(self, window)
        self.setDimensions(30, 30)
        self.setPOS(randrange(800), randrange(200))
        self.window = window
        self.spd = 4
        self.ability = 0

    # Encapsulation Example #
    # MODIFIER METHODS #
    def move(self): # move function
        self.setY(self.y + self.spd)
        if self.y > 590:
            self.setPOS(900, 700)
            self.setDimensions(0, 0)

    def setPowerup(self): # define whether it is a good powerup or bad powerup
        if randrange(2) == 1:
            self.setDimensions(30, 30)
            self.color = GREEN
            self.sprite.fill(self.color)
            self.ability = 15
        else:
            self.setDimensions(30, 30)
            self.color = RED
            self.sprite.fill(self.color)
            self.ability = -15


