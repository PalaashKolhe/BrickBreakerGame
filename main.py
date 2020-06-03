# main.py

'''
title: Brick Breaker
author: Palaash Kolhe
date created: 2020-06-01
'''

from engine import Engine
from pygame import init

if __name__ == "__main__":
    init()
    game = Engine()
    game.run()