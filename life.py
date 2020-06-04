# life.py

'''
title: Life Counter Sprite
'''

from text import Text

class Lives(Text):
    def __init__(self, window):
        Text.__init__(self, "Lives Left: 3", window)
        self.lives = 3

    # MODIFIER METHODS #
    def updateLives(self, num):
        self.lives += num
        self.setText("Lives Left: " + str(self.lives))

    def editLives(self, life):
        self.lives = life
        self.setText("Lives Left: " + str(self.lives))

    # ACCESSOR METHODS #
    def getLives(self):
        return self.lives

