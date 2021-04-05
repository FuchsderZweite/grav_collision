import pygame
import numpy as np
import math
import object as obj


WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600
FPS = 60
NUMBER_OF_OBJECTS = 5

RED = (255, 0, 0)
ORANGE = (239, 131, 84)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
VIOLET = (95, 75, 182)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)

circles = [obj.Circle() for i in range(NUMBER_OF_OBJECTS)]






def redraw_window(screen, dt):
    screen.fill(WHITE)
    for i in circles:
        i.update(dt)
        i.draw(screen)


def collision():
    list_balls = []





    for i in circles[0:-2]:
        for j in circles[1:-1]:
            if(i.id == j.id):
                pass
            else:
                circ1 = circles[i.id]
                circ2 = circles[j.id]
                dist_x = abs(circ1.px - circ2.px)
                dist_y = abs(circ1.py - circ2.py)
                if(dist_x * dist_x + dist_y * dist_y < circ1.radius + circ2.radius ):
                    print("collision between {} and {} ".format(circ1.id, circ2.id))
                    list_balls = list_balls[i.id]
                    list_balls = list_balls[j.id]
                else:
                    pass
    return list_balls




def main():
    pygame.init()

    scaling = 0.00001
    dt = clock.tick(60) * scaling * FPS
    running = True



    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



        redraw_window(screen, dt)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
