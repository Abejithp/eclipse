import pygame
from scripts.utils import load_image, Animation


BASE_PATH = 'assets/'

class PhysicalEntity:
    def __init__(self, position, dimesions, speed=1.5):
        x, y = position
        width, height = dimesions
        self.rect = pygame.Rect(x, y, width, height)
        self.position = list(position)
        self.dimensions = dimesions
        self.velocity = [0,0]
        self.speed = speed
        self.flip = False
        self.animations = {
            'idle_down': Animation('Character/Player/idle_down', 8, True),
            'idle_up': Animation('Character/Player/idle_up', 8, True),
            'idle_right': Animation('Character/Player/idle_right', 8, True),
            'run_down': Animation('Character/Player/run_down', 8, True),
            'run_right': Animation('Character/Player/run_right', 8, True),
            'run_up': Animation('Character/Player/run_up', 8, True),
            'attack_down': Animation('Character/Player/attack_down', 12, True),
            'attack_right': Animation('Character/Player/attack_right', 12, True),
            'attack_up': Animation('Character/Player/attack_up', 12, True),
        }
        self.current_animation = 'idle'
        self.direction = 'down'
        self.attack_frame = 0


    def load_image(self, name):
        return pygame.image.load(BASE_PATH + name).convert()

    def move(self, x, y):
        self.velocity[0] = x
        self.velocity[1] = y
        self.position[0] += x * self.speed
        self.position[1] += y * self.speed
        if x > 0:
            self.current_animation = 'run'
            self.direction = 'right'
            self.flip = False
        elif x < 0:
            self.flip = True
            self.current_animation = 'run'
            self.direction = 'right'
        elif y > 0:
            self.current_animation = 'run'
            self.direction = 'down'
        elif y < 0:
            self.current_animation = 'run'
            self.direction = 'up'
        else:
            self.current_animation = 'idle'
        
    def attack(self):
        self.current_animation = 'attack'
        self.attack_frame = 4
        pass

    def render(self, screen: pygame.Surface):
        animation_frame = self.current_animation + '_' + self.direction

        if self.attack_frame > 0:
            if self.flip:
                screen.blit(pygame.transform.flip(self.animations[animation_frame].img(), True, False), self.position)
            else:
                screen.blit(self.animations[animation_frame].img(), self.position)
            self.animations[animation_frame].update()
            self.attack_frame -= 1
            return

        if self.flip:
            screen.blit(pygame.transform.flip(self.animations[animation_frame].img(), True, False), self.position)
        else:
            screen.blit(self.animations[animation_frame].img(), self.position)
        self.animations[animation_frame].update()
        self.current_animation = 'idle'

