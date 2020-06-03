# engine.py

'''
title: Engine that glues all objects together
'''

from window import Window
from box import Box
from text import Text
import pygame

class Engine:
    def __init__(self):
        self.window = Window()

        # Spawning player bar in
        self.player = Box(self.window)
        self.player.setDimensions(78, 16)
        self.player.setPOS(self.player.window.getWidth() / 2 - self.player.width / 2,
                           self.player.window.getHeight() - self.player.height / 2 - 20)

        # Spawning ball in
        self.ball = Box(self.window)
        self.ball.setDimensions(8, 8)
        self.ball.setPOS(self.ball.window.getWidth() / 2 - self.ball.width / 2,
                         self.ball.window.getHeight() - self.ball.height / 2 - 45)

        # Spawning text in
        self.text = Text("Press SPACE to start!", self.window)
        self.text.setPOS(self.text.window.getWidth() / 2 - self.text.width / 2 - 43,
                         self.text.window.getHeight() - self.text.height / 2 - 65)




        # self.title = Text("Brick Breaker", self.window)
        self.running = True

    def run(self):
        while self.running:
            # INPUTS #
            self.window.getEvents()

            # PROCESSING #
            self.player.move(self.window.getKeyPressed())

            # OUTPUTS #
            self.window.clearScreen()
            self.window.blitSprite(self.player)
            self.window.blitSprite(self.ball)
            self.window.blitSprite(self.text)

            # self.window.blitSprite(self.title)
            self.window.updateScreen()





