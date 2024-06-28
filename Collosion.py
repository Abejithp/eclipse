from typing import List
import pygame
from Collectibles import Bomb
from enum import Enum

class WALLSIDE(Enum):
    TOP = 1
    BOTTOM = 2
    LEFT = 3
    RIGHT = 4

class Wall:
    def __init__(self, x, y, width, height, side):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.side = side
        self.rect = pygame.Rect(x, y, width, height)

    def collide(self, rect):
        return self.rect.colliderect(rect)


class Collosions:
    def __init__(self, width, height):

        self.walls = {
            WALLSIDE.TOP: Wall(0, 0, width, 1, WALLSIDE.TOP),
            WALLSIDE.BOTTOM: Wall(0, height-1, width, 1, WALLSIDE.BOTTOM),
            WALLSIDE.LEFT: Wall(0, 0, 1, height, WALLSIDE.LEFT),
            WALLSIDE.RIGHT: Wall(width-1, 0, 1, height, WALLSIDE.RIGHT)
        }

        self.bombs: List[Bomb] = []
    
    def add_bomb(self, bomb):
        self.bombs.append(bomb)
    
