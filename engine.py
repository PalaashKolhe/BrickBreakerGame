# engine.py

'''
title: Engine that glues all objects together
'''

from window import Window
from box import Box, checkCollision
from text import Text
from loader import *
from score import Score
from pygame import K_SPACE

class Engine:
    def __init__(self):
        self.window = Window()

        # Spawning title box in
        self.titleBox = Box(self.window)
        self.titleBox.setDimensions(800, 35)
        self.titleBox.setPOS(0,0)
        self.titleBox.color = BLACK
        self.titleBox.updateSprite()

        # Spawning title in
        self.title = Text("BRICK BREAKER!", self.window)
        self.title.setPOS(self.title.window.getWidth() / 2 - 75,
                          3)

        # Spawning score in
        self.score = Score(self.window)
        self.score.setPOS(3, 3)

        # Spawning player bar in
        self.player = Box(self.window)
        self.player.setDimensions(100, 20)
        self.player.setPOS(self.player.window.getWidth() / 2 - self.player.width / 2,
                           self.player.window.getHeight() - self.player.height / 2 - 20)

        # Spawning ball in
        self.ball = Box(self.window)
        self.ball.setDimensions(10, 10)
        self.ball.setPOS(self.ball.window.getWidth() / 2 - self.ball.width / 2,
                         self.ball.window.getHeight() - self.ball.height / 2 - 45)

        # Spawning text in
        self.text = Text("Press SPACE to start!", self.window)
        self.text.setPOS(self.text.window.getWidth() / 2 - self.text.width / 2 - 43,
                         self.text.window.getHeight() - self.text.height / 2 - 65)

        self.boxArray = []

        self.running = True
        self.gameStart = False

    def levelCreator(self):
        x = 110 # initial starting point in x plane
        y = 80 # initial starting point in y plane
        length = 100
        height = 40

        rows = 0
        for j in range(y, y + (height * 6), height + 5):
            for i in range(x, x + (length * 6), length + 5):
                box = Box(self.window)
                box.setDimensions(length, height)
                if rows % 2 == 0:
                    box.setPOS(i, j)
                else:
                    box.setPOS(i - 50, j)
                self.boxArray.append(box)
            rows += 1

    def run(self):
        self.levelCreator()
        while self.running:
            # INPUTS #
            self.window.getEvents()

            # PROCESSING #
            self.player.move(self.window.getKeyPressed())

            # OUTPUTS #
            self.window.clearScreen()

            self.window.blitSprite(self.titleBox)
            self.window.blitSprite(self.title)

            self.window.blitSprite(self.score)

            self.window.blitSprite(self.player)
            self.window.blitSprite(self.ball)
            self.window.blitSprite(self.text)

            for i in range(len(self.boxArray)):
                self.window.blitSprite(self.boxArray[i])

            self.window.updateScreen()

            ### GAME STARTS HERE ###
            # PROCESSING #
            if self.window.getKeyPressed()[K_SPACE] == 1: # game start
                self.text.setText('')
                self.gameStart = True

            if self.gameStart:
                ## Ball Movement
                self.ball.autoMove()


                ## Check if ball hits boxes
                for i in range(len(self.boxArray)):
                    if checkCollision(self.ball, self.boxArray[i]):
                        self.boxArray.pop(i)
                        break





