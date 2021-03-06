# engine.py

'''
title: Engine that glues all objects together
'''

from window import Window
from box import Box
from text import Text
from loader import *
from score import Score
from pygame import K_SPACE
from life import Lives
from time import sleep
from powerups import Powerups
from random import randrange

class Engine: # class that aggregates all objects together to make one big grouped object. This is also an example of composition.
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

        # Spawning life counter in
        self.lives = Lives(self.window)
        self.lives.setPOS(self.window.getWidth() - 107, 3)

        # Spawning score in
        self.score = Score(self.window)
        self.score.setPOS(3, 3)

        # Spawning game over text in
        self.gameOver = Text("GAME OVER", self.window, 0, 0, 'Arial', 80)
        self.gameOver.color = RED
        self.gameOver.renderText()
        self.gameOver.setPOS(self.window.getWidth() / 2 - 185, self.window.getHeight() / 2 - 50)

        # Spawning player bar in
        self.player = Box(self.window)
        self.player.setDimensions(100, 20)
        self.player.setSpeed(12)
        self.player.setPOS(self.player.window.getWidth() / 2 - self.player.width / 2,
                           self.player.window.getHeight() - self.player.height / 2 - 20)

        # Spawning ball in
        self.ball = Box(self.window)
        self.ball.setDimensions(10, 10)
        self.ball.setPOS(self.ball.window.getWidth() / 2 - self.ball.width / 2,
                         self.ball.window.getHeight() - self.ball.height / 2 - 45)

        # Spawning text in
        self.text = Text('''Press SPACE to start!       A = Move Left      D = Move Right''', self.window)
        self.text.setPOS(self.window.getWidth() / 2 - self.text.width / 2 - 210,
                         self.window.getHeight() - self.text.height / 2 - 65)

        self.boxArray = []

        self.running = True
        self.playing = True
        self.gameStart = False
        self.restartVar = False

        # Spawning Level Complete Message
        self.levelComplete = Text("Proceeding to Next Level", self.window, 0, 0, 'Arial', 50)
        self.levelComplete.renderText()
        self.levelComplete.setPOS(self.window.getWidth() / 2 - 220, self.window.getHeight() / 2 - 50)

        # Spawning -1 life
        self.lifeLostText = Text("Lost 1 life. Press space to start again", self.window)
        self.lifeLostText.renderText()
        self.lifeLostText.setPOS(self.window.getWidth() / 2 - 160, self.window.getHeight() - 115)

        # creating power up array
        self.powerupArray = []
        for i in range(5):
            powerup = Powerups(self.window)
            powerup.setPowerup()
            self.powerupArray.append(powerup)

        # timer for powerup drops
        self.timer = 0

    def levelCreator(self):
        x = 110 # initial starting point in x plane
        y = 80 # initial starting point in y plane
        length = 100
        height = 40

        rows = 0 # var to alternate x starting points between each row
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

    def restart(self): # restart function for when ball touches ground
        self.gameStart = False
        self.lifeLostText.setText("Lost 1 life. Press space to start again")
        self.ball.restartPositionBall()
        self.player.restartPositionPlayer()
        self.restartVar = True

    def run(self):
        global powerup # local var for powerup
        self.levelCreator() # create bricks
        while self.running:
            # INPUTS #
            self.window.getEvents()

            # PROCESSING #
            self.player.move(self.window.getKeyPressed()) # example of polymorphism. Achieves different outcome from move() function in powerups file
            finalWindowUpdate = False # for the program to update and blit everything one last time before displaying game over. Mainly to update lives left

            # OUTPUTS #
            self.window.clearScreen()
            self.window.blitSprite(self.titleBox)
            self.window.blitSprite(self.title)
            self.window.blitSprite(self.score)
            self.window.blitSprite(self.lives)
            self.window.blitSprite(self.player)
            self.window.blitSprite(self.ball)
            self.window.blitSprite(self.text)
            for i in range(len(self.boxArray)): # blit all the bricks onto window
                self.window.blitSprite(self.boxArray[i])
            try: # blit powerup into window
                self.window.blitSprite(powerup)
            except NameError:
                pass
            if not self.playing: # so window updates one last time before displaying game over. This is required to blit lives onto window
                finalWindowUpdate = True
            if self.restartVar and not finalWindowUpdate: # so "play again" only displays when a life is lost. If there are no lives left, nothing is displayed.
                self.window.blitSprite(self.lifeLostText)
            self.window.updateScreen()

            if self.playing:
                ### GAME STARTS HERE ###
                # PROCESSING #
                if self.window.getKeyPressed()[K_SPACE] == 1: # game start
                    self.text.setText('') # to remove text from screen
                    self.lifeLostText.setText('') # to remove text from screen
                    self.gameStart = True

                if self.gameStart:
                    ## Ball Movement
                    self.ball.autoMove()

                    ## Check if ball hits bottom
                    if self.ball.getY() > 590:
                        self.lives.updateLives(-1)
                        self.restart()

                    ## Check if lives are 0
                    if self.lives.getLives() == 0:
                        self.playing = False

                    ## Check if ball hits boxes
                    if self.ball.checkCollision(self.player): # check if ball hits player bar
                        self.ball.dirY *= -1
                        self.ball.setY(self.ball.getY() - 5)

                    if self.ball.checkCollision(self.titleBox): # check if ball hits top title bar
                        self.ball.dirY *= -1
                        self.ball.setY(self.ball.getY() + 5)

                    for i in range(len(self.boxArray)): # check if ball hits bricks
                        if self.ball.checkCollision(self.boxArray[i]):
                            self.ball.checkCollisionSide(self.boxArray[i])
                            self.score.updateScore(20)
                            self.boxArray.pop(i) # remove brick from array, thereby removing the brick from the screen
                            break

                    self.timer += 1 # timer for powerup function
                    if self.timer == 100: # powerups spawn between every 100 intervals
                        powerup = self.powerupArray[randrange(len(self.powerupArray))]

                    try: # try function in case self.timer doesnt reach 100 and powerup is not defined
                        powerup.move()# example of polymorphism. Achieves different outcome from move() function in box file
                        if self.player.checkCollision(powerup):
                            self.player.setWidth(self.player.getWidth() + powerup.ability) # change width according to powerup
                            self.timer = 0
                            powerup.setPOS(900, 900)
                            del powerup
                        elif powerup.getY() > 600:
                            self.timer = 0
                            powerup.setPOS(900, 900)
                            del powerup
                    except NameError:
                        pass

                    # After winning the game
                    if len(self.boxArray) == 0: # checks if no more boxes left
                        self.window.clearScreen()
                        self.window.blitSprite(self.levelComplete) # print "proceeding to next level"
                        self.window.updateScreen()
                        try:
                            del powerup # remove powerup var so it doesnt stay spawned in the next game
                        except NameError:
                            pass

                        sleep(3) # sleep function so user can read "Proceeding to next level"

                        engine = Engine() # create new game but with values from previous game such as score, lives, and player bar width
                        engine.score.updateScore(self.score.getScore())
                        engine.lives.editLives(self.lives.getLives())
                        engine.ball.setSpeed(self.ball.spd + 2) # increase speed to make game harder
                        engine.player.setSpeed(self.player.spd + 2)
                        engine.player.setWidth(self.player.getWidth())
                        engine.run()

            while not self.playing and finalWindowUpdate: # if player loses
                self.window.getEvents()
                self.window.blitSprite(self.gameOver) # print game over
                self.window.updateScreen()
