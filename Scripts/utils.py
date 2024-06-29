import pygame

BASE_PATH = 'assets/'

def load_image(name):
    return pygame.image.load(BASE_PATH + name).convert()