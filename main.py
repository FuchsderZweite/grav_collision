import pygame
from random import randint

pygame.init()
white = (255,255,255)
black = (0,0,0)

WIDTH = 800
HEIGHT = 600
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    surf = pygame.Surface((50, 50))
    surf.fill((0, 0, 0))
    rect = surf.get_rect()




class Object:
    def __init__(self):
        self.mass = randint(20,100)
        self.pos_x = randint(0, WIDTH)
        self.pos_y = randint(0, HEIGHT)

#pygame.display.update()
#clock.tick(FPS)

#def game_loop():
#    game_exit = False
#    game_over = False

pygame.quit()
quit()

#game_loop()