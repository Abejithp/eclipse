import pygame
from os.path import join
from RigidBody import Player
from Collosion import Wall, Collosions
from Collectibles import Bomb

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 450
FPS = 60 
VELOCITY = 10

monitor_size = pygame.display.Info()

pygame.display.set_caption("Blossom")
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((monitor_size.current_w, monitor_size.current_h), pygame.FULLSCREEN)

def draw(screen: pygame.Surface, player: Player, background: list, image: pygame.Surface, bomb: Bomb):

    for tile in background:
        screen.blit(image, tile)

    player.draw(screen)
    player.draw_health(screen)
    bomb.draw(screen)
    pygame.display.update()

def handle_move(player: Player):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        player.move_x(-VELOCITY)
    if keys[pygame.K_d]:
        player.move_x(VELOCITY)
    if keys[pygame.K_w]:
        player.move_y(-VELOCITY)
    if keys[pygame.K_s]:
        player.move_y(VELOCITY)



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

    bomb = Bomb(monitor_size.current_w-200, monitor_size.current_h-200, 50, 50)

    collosions = Collosions(monitor_size.current_w, monitor_size.current_h)
    collosions.add_bomb(bomb)


    fullscreen = False
    background, image = get_background("background.png")

    run=True

    while run:
        clock.tick(FPS)
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.VIDEORESIZE:
                if not fullscreen:
                    width, height = event.dict['size']
                    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    
            if event.type == pygame.KEYDOWN:
                if event.dict.get('key') == pygame.K_ESCAPE:
                    run = False
                if event.dict.get('key') == pygame.K_LALT:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode((monitor_size.current_w, monitor_size.current_h), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)

        player.update(FPS, collosions, bomb)

        handle_move(player)
        draw(screen, player, background, image, bomb)
        
    pygame.quit()
    quit()


if __name__ == "__main__":
    main(screen)