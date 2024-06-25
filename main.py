import pygame
from Player import Player
from Objects import Ground

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1000
FPS = 60 
VELOCITY = 5

pygame.display.set_caption("Blossom")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def draw(screen: pygame.Surface, player: Player, ground: Ground):

    player.draw(screen)
    ground.draw(screen)
    pygame.display.update()

def handle_move(player: Player):
    keys = pygame.key.get_pressed()

    player.x_vel = 0

    if keys[pygame.K_a]:
        player.move_left(VELOCITY)
    if keys[pygame.K_d]:
        player.move_right(VELOCITY)


def main(screen: pygame.Surface):
    clock = pygame.time.Clock()
    player = Player()
    ground = Ground(0, 800, 1920, 20)
    run=True

    while run:
        clock.tick(FPS)
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.jump_count < 2:
                    player.jump()

        player.update(FPS, ground)
        handle_move(player)
        draw(screen, player, ground)
        
    pygame.quit()
    quit()


if __name__ == "__main__":
    main(screen)