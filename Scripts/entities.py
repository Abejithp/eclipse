import pygame
from Scripts.utils import load_image, Animation


BASE_PATH = 'assets/'

class PhysicalEntity:
   
    def __init__(self, position, dimesions, speed=1):
        x, y = position
        width, height = dimesions
        self.rect = pygame.Rect(x, y, width, height)
        self.position = list(position)
        self.dimensions = dimesions
        self.velocity = speed
        self.animations = {
            'idle': Animation('Character/Player/idle', 8, True),
        }
        self.current_animation = 'idle'


    def load_image(self, name):
        return pygame.image.load(BASE_PATH + name).convert()
    

    def move(self, x, y):
        self.position[0] += x * self.velocity
        self.position[1] += y * self.velocity
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]

    def render(self, screen: pygame.Surface):
        screen.blit(self.animations['idle'].img(), self.position)
        self.animations[self.current_animation].update()