# box.py

'''
title: Box Sprites
'''

from sprites import Sprite
from pygame import K_d, K_a
import pygame

class Box(Sprite):
    def __init__(self, window):
        Sprite.__init__(self, window)
        self.setDimensions(150, 50)
        self.setPOS(self.window.getWidth() / 2 - self.width / 2,
                    self.window.getHeight() / 2 - self.height / 2)

        self.spd = 10

    def move(self, keys):
        if keys[K_d]  == 1:
            self.x += self.spd
        elif keys[K_a] == 1:
            self.x -= self.spd

        if self.x > self.window.getWidth() - self.sprite.get_rect().width:
            self.x = self.window.getWidth() - self.sprite.get_rect().width
        elif self.x < 0:
            self.x = 0

        if self.y > self.window.getHeight() - self.sprite.get_rect().height:
            self.y = self.window.getHeight() - self.sprite.get_rect().height
        elif self.y < 0:
            self.y = 0

        self.pos = (self.x, self.y)

    def autoMove(self):
        self.setPOS(self.getX() + (self.spd * self.dirX), self.getY() + (self.spd * self.dirY))
        if self.getX() > self.window.getWidth() - self.getWidth():
            self.dirX = -1
        elif self.getX() < 0:
            self.dirX = 1
        if self.getY() > self.window.getHeight() - self.getHeight():
            self.dirY = -1
        elif self.getY() < 0:
            self.dirY = 1

    # def autoMoveCollisions(self):


def checkCollision(box1, box2):
    return box1.sprite.get_rect(x = box1.getX(), y = box1.getY()).colliderect(box2.sprite.get_rect(x = box2.getX(), y = box2.getY()))

if __name__ == "__main__":
    from window import Window
    from pygame import init

    init()

    window = Window()
    box = Box(window)

    while True:
        window.getEvents()
        box.move(window.getKeyPressed())
        window.clearScreen()
        window.blitSprite(box)
        window.updateScreen()