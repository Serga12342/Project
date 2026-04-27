import pygame
import sys
from player import Player
from maps import draw_map
from engine import Engine

pygame.init()
clock = pygame.time.Clock()
FPS = 60

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

BLUE = (30, 144, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 215, 0)

player = Player([400, 300], 100, 100, 0, 1)
engine = Engine(screen_width, screen_height)

pygame.display.set_caption("Игра")
pygame.mouse.set_visible(False)
pygame.event.set_grab(True) 

pygame.mouse.get_rel() 


texture = pygame.image.load("texture.jpg").convert()

running = True
visibility = False
grab = True
while running:
    dt = clock.tick(FPS) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                visibility = not visibility
                grab = not grab
                pygame.mouse.set_visible(visibility)
                pygame.event.set_grab(grab)
    

    mouse_dx = pygame.mouse.get_rel()[0]
    sensitivity = 0.1
    player.angle += mouse_dx * sensitivity
    player.angle %= 360


    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player.moove_W(dt)
    if keys[pygame.K_s]:
        player.moove_S(dt)
    if keys[pygame.K_a]:
        player.moove_A(dt)
    if keys[pygame.K_d]:
        player.moove_D(dt)
    
    print(player.coords)

    screen.fill(BLACK)


    pygame.draw.rect(screen, (15, 25, 55), (0, 0, screen_width, screen_height // 2))
    pygame.draw.rect(screen, (30, 30, 35), (0, screen_height // 2, screen_width, screen_height // 2))

    #pygame.draw.circle(screen, BLUE, player.coords, 10, width=0)
    #draw_map(screen, WHITE)
    engine.ray_casting(player.coords, player.angle, YELLOW, screen, texture)
    
    pygame.display.flip()

pygame.quit()
sys.exit()
