# sprites.py
'''
title: Sprites Abstract Class
'''

from pygame import Surface, SRCALPHA

class Sprite:
    def __init__(self, window, x = 0, y = 0):
        self.width = 100
        self.height = 100
        self.dimensions = (self.width, self.height)
        self.sprite = Surface(self.dimensions, SRCALPHA, 32)

        self.red = 255
        self.green = 255
        self.blue = 255
        self.color = (self.red, self.green, self.blue)
        self.sprite.fill(self.color)

        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.window = window
        self.dirX = 1
        self.dirY = 1

        # --- MODIFIER METHODS --- #
        # -- Dimensions -- #

    def updateSprite(self):
        self.dimensions = (self.width, self.height)
        self.sprite = Surface(self.dimensions, SRCALPHA, 32)
        self.sprite.fill(self.color)

    def setWidth(self, width):
        self.width = width
        self.updateSprite()

    def setHeight(self, height):
        self.height = height
        self.updateSprite()

    def setDimensions(self, width, height):
        self.width = width
        self.height = height
        self.updateSprite()

        # -- Positions -- #

    def setX(self, x):
        self.x = x
        self.pos = (self.x, self.y)

    def setY(self, y):
        self.y = y
        self.pos = (self.x, self.y)

    def setPOS(self, x, y):
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)

        # --- ACCESSOR METHODS --- #

    def getSprite(self):
        return self.sprite

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getPOS(self):
        return self.pos