import pygame
from os.path import join
from Player import Player
from Objects import Ground

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1600, 900
FPS = 60 
VELOCITY = 5

pygame.display.set_caption("Blossom")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def draw(screen: pygame.Surface, player: Player, background: list, image: pygame.Surface):

    for tile in background:
        screen.blit(image, tile)

    player.draw(screen)
    pygame.display.update()

def handle_move(player: Player):
    keys = pygame.key.get_pressed()

    player.x_vel = 0

    if keys[pygame.K_a]:
        player.move_left(VELOCITY)
    if keys[pygame.K_d]:
        player.move_right(VELOCITY)



def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []
    
    for x in range(0, SCREEN_WIDTH, width):
        for y in range(0, SCREEN_HEIGHT, height):
            tiles.append((x, y))

    return tiles, image

def main(screen: pygame.Surface):
    clock = pygame.time.Clock()
    player = Player()
    ground = Ground(0, 850, 1600, 20)
    
    background, image = get_background("test.png")

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
        draw(screen, player, background, image)
        
    pygame.quit()
    quit()


if __name__ == "__main__":
    main(screen)