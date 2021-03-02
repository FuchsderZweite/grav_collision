import pygame
import numpy as np
from random import randint


WIDTH = 800
HEIGHT = 800
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
clock = pygame.time.Clock()

NUMBER_OF_OBJECTS = 10
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)


class Circle_Object:
    id_list = []
    COLORS = [(255,255,255), ]
    def __init__(self):
        self.id = len(self.id_list) + 1

        self.mass = randint(10, 100)
        self.radius = randint(10, 40)
        self.pos = pygame.math.Vector2(randint(0+self.radius, WIDTH-self.radius), randint(0+self.radius, HEIGHT-self.radius))
        self.v = pygame.math.Vector2(randint(-15, 15), randint(-15, 15))
        if self.v.x == 0 or self.v.y == 0:
            self.v = pygame.math.Vector2(randint(-15, 15), randint(-15, 15))
        self.a = pygame.math.Vector2(1, 1)
        self.color = (randint(0,255),randint(0,255),randint(0,255))
        # self.gravity = 0.35
        # self.friction = -0.12

    def draw(self, screen):
        self.screen = screen
        pygame.draw.circle(self.screen, self.color, (self.pos.x, self.pos.y), self.radius)

    def update(self, dt):
        self.horizontal_movement(dt)
        self.vertical_movement(dt)

    def horizontal_movement(self, dt):
        #self.velocity.x += self.acceleration.x*dt
        #self.limit_velocity(4)
        #self.position.x += self.velocity.x * dt + (0.5 * self.acceleration.x ) * (dt*dt)
        self.pos.x += self.v.x * dt
        col_left, col_right, col_top, col_bottom = self.collision_check()
        if col_left or col_right:
            self.v.x *= -1
        #elif col_top or col_bottom:
         #   self.v.y *= -1


    def vertical_movement(self, dt):
        #self.velocity.y += self.acceleration.y * dt
        #self.limit_velocity(4)
        #self.position.y += self.velocity.y * dt + (0.5 * self.acceleration.y) * (dt * dt)
        self.pos.y += self.v.y * dt
        col_left, col_right, col_top, col_bottom = self.collision_check()
        if col_top or col_bottom:
            self.v.y *= -1


    def limit_velocity(self, max_v):
        min(-max_v, max(self.v.x, max_v))
        if abs(self.v.x < 0.1):
            self.velocity = 0.0


    def collision_check(self):
        collision_left =  False
        collision_right = False
        collision_top = False
        collision_bottom = False

        if self.pos.x - self.radius <= 0.0:
            collision_left = True
        elif self.pos.x + self.radius >= WIDTH:
            collision_right = True
        elif self.pos.y - self.radius <= 0.0:
            collision_top = True
        elif self.pos.y + self.radius >= HEIGHT:
            collision_bottom = True
        return collision_left, collision_right, collision_top, collision_bottom


    def add_text(self):
        self.screen.blit(self.font.render('Hello!', True, (255, 0, 0)), (200, 100))
        pygame.display.update()

circles = [Circle_Object() for i in range(NUMBER_OF_OBJECTS)]

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
