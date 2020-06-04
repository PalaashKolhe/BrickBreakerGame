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

        self.spd = 8

    # MODIFIER METHODS #
    def setSpeed(self, speed):
        self.spd = speed

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

    def checkCollision(self, box2):
        return self.sprite.get_rect(x = self.getX(), y = self.getY()).colliderect(box2.sprite.get_rect(x = box2.getX(), y = box2.getY()))

    def checkCollisionSide(self, box2):
        topLeft = (self.getX(), self.getY())
        topRight = (self.getX() + self.getWidth(), self.getY())
        bottomLeft = (self.getX(), self.getY() + self.getHeight())
        bottomRight = (self.getX() + self.getWidth(), self.getY() + self.getHeight())

        def ifWriter(coord):
            return box2.sprite.get_rect(x = box2.getX(), y = box2.getY()).collidepoint(coord)

        if ifWriter(topLeft) and ifWriter(topRight):
            self.setY(self.getY() + 5)
            self.dirY *= -1
        elif ifWriter(topLeft) and ifWriter(bottomLeft):
            self.setX(self.getX() + 5)
            self.dirX *= -1
        elif ifWriter(bottomLeft) and ifWriter(bottomRight):
            self.setY(self.getY() -5)
            self.dirY *= -1
        elif ifWriter(bottomRight) and ifWriter(topRight):
            self.setX(self.getX() - 5)
            self.dirX *= -1
        elif ifWriter(topLeft) or ifWriter(topRight):
            self.dirY *= -1
        elif ifWriter(topLeft) or ifWriter(bottomLeft):
            self.dirX *= -1
        elif ifWriter(bottomLeft) or ifWriter(bottomRight):
            self.dirY *= -1
        elif ifWriter(bottomRight) or ifWriter(topRight):
            self.dirX *= -1


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