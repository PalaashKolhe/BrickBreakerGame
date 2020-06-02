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
        self.player = Box(self.window)
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
            # self.window.blitSprite(self.title)
            self.window.updateScreen()





