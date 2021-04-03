import pygame
import math
import object as obj


WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600
FPS = 60
NUMBER_OF_OBJECTS = 3

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)

circles = [obj.Circle() for i in range(NUMBER_OF_OBJECTS)]

def collision():
    for i in circles[0:-2]:
        for j in circles[1:-1]:
            if(i.id == j.id):
                pass
            else:
                circ1 = circles[i.id]
                circ2 = circles[j.id]
                dist_x = abs(circ1.pos.x - circ2.pos.x)
                dist_y = abs(circ1.pos.y - circ2.pos.y)
                #dist_abs = math.sqrt(dist_x**2 + dist_y**2)             # avoid sqrt()
                if(dist_x * dist_x + dist_y * dist_y < circ1.radius + circ2.radius ):
                    print("collision between{} and {} ".format(circ1.id, circ2.id))

                else:
                    pass





def redraw_window(screen):
    screen.fill((0, 0, 0))

    p1_camera = pygame.Rect(0, 0, 400, 300)

    screen.blit(screen, (0, 0), p1_camera)

    for i in circles:
        i.draw(screen)

def main():
    pygame.init()
    #font = pygame.font.SysFont(None, 30)
    scaling = 0.00001
    dt = clock.tick(60) * scaling * FPS
    running = True




    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        redraw_window(screen)
        pygame.display.flip()
        for i in circles:
            collision()
            i.update(dt)
        clock.tick(FPS)
    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
