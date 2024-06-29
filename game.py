import sys
import pygame
from Scripts.entities import PhysicalEntity

class Game:
    def __init__(self):
        scale = 3
        pygame.init()
        pygame.display.set_caption("Eclipse")
        self.screen = pygame.display.set_mode((1280,720))
        self.clock = pygame.time.Clock()
        self.display = pygame.Surface((1280// scale, 720// scale))
        self.player = PhysicalEntity((100,100), (13,20))

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player.move(0, -1)
        if keys[pygame.K_s]:
            self.player.move(0, 1)
        if keys[pygame.K_a]:
            self.player.move(-1, 0)
        if keys[pygame.K_d]:
            self.player.move(1, 0)
        

    def start(self):
        while True:
            self.display.fill((150,0,0))
            self.player.render(self.display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.handle_input()

            self.screen.blit(pygame.transform.scale(self.display, (1280, 720)), (0,0))
            pygame.display.update()
            self.clock.tick(60)
        



if __name__ == '__main__':
    Game().start()