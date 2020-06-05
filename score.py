# score.py

'''
title: Score Text Sprite
'''

from text import Text

class Score(Text): # Concrete child class (inheriting from class Text)
    def __init__(self, window):
        Text.__init__(self, "Score: 0", window)
        self.score = 0

    # Encapsulation Example #
    # MODIFIER METHODS #
    def updateScore(self, newScore): # add score
        self.score += newScore
        self.setText("Score: " + str(self.score))

    # ACCESSOR METHODS #
    def getScore(self): # get score
        return self.score



