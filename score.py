# score.py

'''
title: Score Text Sprite
'''

from text import Text

class Score(Text):
    def __init__(self, window):
        Text.__init__(self, "Score: 0", window)
        self.score = 0

    # MODIFIER METHODS #
    def updateScore(self, newScore):
        self.score += newScore
        self.setText("Score: " + str(self.score))

    # ACCESSOR METHODS #
    def getScore(self):
        return self.score



