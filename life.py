# life.py

'''
title: Life Counter Sprite
'''

from text import Text

class Lives(Text): # Concrete child class (inheriting from class Text)
    def __init__(self, window):
        Text.__init__(self, "Lives Left: 3", window)
        self.lives = 3

    # Encapsulation Example #
    # MODIFIER METHODS #
    def updateLives(self, num): # subtract lives
        self.lives += num
        self.setText("Lives Left: " + str(self.lives))

    def editLives(self, life): # redefine lives
        self.lives = life
        self.setText("Lives Left: " + str(self.lives))

    # ACCESSOR METHODS #
    def getLives(self): # get lives
        return self.lives

