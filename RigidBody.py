from typing import Dict, List
from enum import Enum
import pygame
from Collosion import Wall, Collosions
from Collectibles import Bomb

from Collosion import WALLSIDE
from os.path import join


class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4


class Character:
    def __init__(self, health, x, y, width, height, name):
        self.health = health
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.collected_damage = 0
        self.mask = None
        self.direction = Direction.DOWN
        self.sprite = pygame.image.load(join("assets", "Characters", "Player", name))

    def move(self, dx, dy):
        self.x_vel = dx
        self.y_vel = dy

    def move_x(self, vel):
        
        self.direction = Direction.LEFT if vel < 0 else Direction.RIGHT
        self.rect.x += vel

    def move_y(self, vel):
        self.direction = Direction.UP if vel < 0 else Direction.DOWN
        self.rect.y += vel


class Player(Character):
    def __init__(self, x, y, name):
        super().__init__(1000, x, y, 150, 150, name)

    def draw_health(self, screen: pygame.Surface):
        pygame.draw.rect(screen, (255,0,0), (0, 0, 1000, 20))
        pygame.draw.rect(screen, (0,255,0), (0, 0, self.health, 20))

    def collect_damage(self, damage):
        self.collected_damage += damage
    
    def take_damage(self, damage):
        self.health -= damage



    def check_walls(self, walls: Dict[WALLSIDE, Wall]):
        if walls[WALLSIDE.TOP].collide(self.rect):
            self.rect.y = walls[WALLSIDE.TOP].rect.y + walls[WALLSIDE.TOP].rect.height
            self.y_vel = 0

        if walls[WALLSIDE.BOTTOM].collide(self.rect):
            self.rect.y = walls[WALLSIDE.BOTTOM].rect.y - self.rect.height
            self.y_vel = 0

        if walls[WALLSIDE.LEFT].collide(self.rect):
            self.rect.x = walls[WALLSIDE.LEFT].rect.x + walls[WALLSIDE.LEFT].rect.width
            self.x_vel = 0

        if walls[WALLSIDE.RIGHT].collide(self.rect):
            self.rect.x = walls[WALLSIDE.RIGHT].rect.x - self.rect.width
            self.x_vel = 0
                

    def check_bombs(self, bombs: List[Bomb]):
        for bomb in bombs:
            if bomb.active and bomb.collide(self.rect):
                self.collect_damage(bomb.damage)
                bomb.remove()
   
    
    def update(self, fps, collosions: Collosions):
        self.move(self.x_vel, self.y_vel)
        self.check_walls(collosions.walls)
        self.check_bombs(collosions.bombs)

        if(self.collected_damage > 0):
            self.health -= 2
            self.collected_damage -= 2

    def draw(self, screen: pygame.Surface):
        screen.blit(self.sprite, (self.rect.x, self.rect.y))
        # pygame.draw.rect(screen, (255,0,0), self.rect)



    
