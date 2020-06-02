# main.py

'''
title: Boxes 2.0
author: Palaash Kolhe
date created: 2020-05-23
'''

from engine import Engine
from pygame import init

if __name__ == "__main__":
    init()
    game = Engine()
    game.run()