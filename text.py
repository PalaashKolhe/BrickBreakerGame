# text.py

'''
title: Text Sprites
'''

from sprites import Sprite
from loader import *
from pygame import font

class Text(Sprite): # Concrete child class / concrete parent class (inheriting from class Sprite)
    def __init__(self, content, window, x = 0, y = 0, fontFam = "Arial", fontSize = 24):
        Sprite.__init__(self, window, x, y)
        self.content = content
        self.fontFam = fontFam
        self.fontSize = fontSize
        self.color = WHITE
        self.font = font.SysFont(self.fontFam, self.fontSize)
        self.sprite = self.font.render(self.content, 1, self.color)

    # Encapsulation Example #
    # --- MODIFIER METHODS --- #

    def renderText(self): # render text on screen
        self.font = font.SysFont(self.fontFam, self.fontSize)
        self.sprite = self.font.render(self.content, 1, self.color)

    def setText(self, content): # set content in text
        self.content = content
        self.renderText()