# window.py

'''
title: Pygame Window Frame
'''

import pygame
from loader import *

class Window:
    def __init__(self):
        self.title = TITLE
        self.fps = FPS
        self.width = WIDTH
        self.height = HEIGHT
        self.screenDimensions = (self.width, self.height)
        self.background = GREY
        self.frame = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.screenDimensions)
        self.screen.fill(self.background)
        self.caption = pygame.display.set_caption(self.title)
        self.keysPressed = None

    # --- Modifier Methods --- #
    def run(self):
        while True:
            # INPUTS #
            self.getEvents()
            # OUTPUTS #
            self.clearScreen()
            self.updateScreen()

    def updateScreen(self):
        self.frame.tick(self.fps)
        pygame.display.flip()

    def clearScreen(self):
        self.screen.fill(self.background)

    def blitSprite(self, sprite):
        self.screen.blit(sprite.getSprite(), sprite.getPOS())

    # --- ACCESSOR METHODS --- #
    def getEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        self.keysPressed = pygame.key.get_pressed()

    def getWidth(self):
        return self.screen.get_rect().width

    def getHeight(self):
        return self.screen.get_rect().height

    def getKeyPressed(self):
        return self.keysPressed








