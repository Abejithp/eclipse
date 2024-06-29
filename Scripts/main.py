import pygame
from os.path import join
from RigidBody import Player
from Collosion import Collosions
from Collectibles import Bomb
from Camera import Camera

pygame.init()


SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
FPS = 60 
VELOCITY = 6

monitor_size = pygame.display.Info()

pygame.display.set_caption("Blossom")
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((monitor_size.current_w, monitor_size.current_h), pygame.FULLSCREEN)

def draw(screen: pygame.Surface, player: Player, bomb: Bomb, camera: Camera):

    screen.fill((25,70,26), (0, 0, monitor_size.current_w, monitor_size.current_h))
    camera.draw(screen, (player.rect.x, player.rect.y))


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




def main(screen: pygame.Surface):
    clock = pygame.time.Clock()
    player = Player(10, 10, "player.png")
    player.load_sprite()
    bomb = Bomb(monitor_size.current_w-200, monitor_size.current_h-200, 50, 50)
    collosions = Collosions(monitor_size.current_w, monitor_size.current_h)
    collosions.add_bomb(bomb)

    camera = Camera(monitor_size.current_w, monitor_size.current_h, "background.png", 0, 0)
    camera.get_background()
    fullscreen = False

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

        player.update(FPS, collosions)
        handle_move(player)
        draw(screen, player, bomb, camera)
        
    pygame.quit()
    quit()


if __name__ == "__main__":
    main(screen)