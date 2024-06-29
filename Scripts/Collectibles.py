import pygame

class Collectible:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)



    def collide(self, rect):
        return self.rect.colliderect(rect)

    def move(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen: pygame.Surface, image: pygame.Surface):
        screen.blit(image, (self.x, self.y))

class Bomb(Collectible):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.damage = 400
        self.active = True
    
    def remove(self):
        self.active = False
        self.x = -100
        self.y = -100


    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, (255,50,50), (self.x, self.y, self.width, self.height))