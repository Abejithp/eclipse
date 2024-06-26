import pygame
from Objects import Boundaries



class Player:
    GRAVITY = 1
    def __init__(self):
        self.health = 100
        self.rect = pygame.Rect((300, 250, 150, 300))
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None

        self.fall_count = 0
        self.jump_count = 0


    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, vel):
        self.x_vel = -vel

    def move_right(self, vel):
        self.x_vel = vel

    def jump(self):
        self.y_vel = -self.GRAVITY * 10
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0
        

    
    def update(self, fps, ground: Boundaries, left_wall: Boundaries, right_wall: Boundaries):
        self.move(self.x_vel, self.y_vel)
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.fall_count += 1

        if ground.collide(self.rect):
            self.rect.y = ground.rect.y - self.rect.height
            self.fall_count = 0
            self.y_vel = 0
            self.jump_count = 0

        if left_wall.collide(self.rect):
            self.rect.x = left_wall.rect.x + left_wall.rect.width
            self.x_vel = 0

        if right_wall.collide(self.rect):
            self.rect.x = right_wall.rect.x - self.rect.width
            self.x_vel = 0
        

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, (255,0,0), self.rect )
