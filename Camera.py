import pygame
from RigidBody import Player
from Collectibles import Bomb
from os.path import join

class Camera:
    def __init__(self, width, height, name, posX, posY):
        self.width = width
        self.height = height
        self.background = None
        self.image = pygame.image.load(join("assets", "Background", name))
        self.posX = posX
        self.posY = posY
    


    def get_background(self):
        image = self.image
        _, _, width, height = image.get_rect()
        tiles = []
        
        for x in range(0, self.width, width):
            for y in range(0, self.height, height):
                tiles.append((x, y))

        self.background = tiles
    
    def draw(self, screen: pygame.Surface, position: tuple):
        self.posX, self.posY = position
    
        for tile in self.background:
            screen.blit(self.image, (tile[0] - self.posX*2//3, tile[1] - self.posY*2//3))
