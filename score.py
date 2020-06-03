# score.py

'''
title: Score Text Sprite
'''

from text import Text

class Score(Text):
    def __init__(self, window):
        Text.__init__(self, "Score: 0", window)
        self.score = 0
        self.content = "Score: 0"

    # MODIFIER METHODS #
    def updateScore(self, newScore):
        self.score += newScore
        self.setText(self.content + str(self.score))
        self.renderText()

    # ACCESSOR METHODS #
    def getScore(self):
        return self.score



