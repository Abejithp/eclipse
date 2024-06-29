import pygame



BASE_PATH = 'assets/'

class PhysicalEntity:
   

    def __init__(self, position, dimesions, speed=8):
        x, y = position
        width, height = dimesions
        self.rect = pygame.Rect(x, y, width, height)
        self.position = list(position)
        self.dimensions = dimesions
        self.velocity = speed


    def load_image(self, name):
        return pygame.image.load(BASE_PATH + name).convert()

    def move(self, x, y):
        self.position[0] += x * self.velocity
        self.position[1] += y * self.velocity
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]

    def render(self, screen: pygame.Surface):
        pygame.draw.rect(screen, (255,50,50), (self.position[0], self.position[1], self.dimensions[0], self.dimensions[1]))