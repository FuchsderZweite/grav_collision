import pygame
import object as obj


WIDTH = 600
HEIGHT = 600
FPS = 60
NUMBER_OF_OBJECTS = 10

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)

circles = [obj.Circle(HEIGHT, WIDTH) for i in range(NUMBER_OF_OBJECTS)]

def redraw_window(screen):
    screen.fill((0, 0, 0))
    for i in circles:
        i.draw(screen)

def main():
    pygame.init()
    font = pygame.font.SysFont(None, 30)
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
            i.update(dt)
        clock.tick(FPS)
    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
