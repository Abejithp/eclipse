import pygame
from os import listdir
from os.path import join, isfile
BASE_PATH = 'assets/'

def load_image(name):
    path = join(BASE_PATH, name)
    images = [f for f in listdir(path) if isfile(join(path, f))]
    return [pygame.image.load(join(path, img)).convert_alpha() for img in images]


class Animation:
    def __init__(self, name, duration, loop=True):
        self.images = load_image(name)
        self.duration = duration
        self.loop = loop
        self.completed = False
        self.frame = 0
    
    def img(self):
        return self.images[int(self.frame / self.duration)]
    
    def update(self):
        if self.loop:
            self.frame = (self.frame + 1) % (len(self.images) * self.duration)
        else:
            self.frame += 1
            if self.frame >= len(self.images) * self.duration:
                self.completed = True
                self.frame = len(self.images) * self.duration - 1