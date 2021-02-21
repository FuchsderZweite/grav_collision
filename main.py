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

NUMBER_OF_OBJECTS = 2
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)


class Circle_Object:
    def __init__(self):
        self.mass = randint(20, 100)
        self.radius = randint(10, 40)
        self.gravity = 0.35
        self.friction = -0.12
        self.position = pygame.math.Vector2(randint(0+self.radius, WIDTH-self.radius), randint(0+self.radius, HEIGHT-self.radius))
        self.velocity = pygame.math.Vector2(randint(-10, 10), randint(-10, 10))
        self.acceleration = pygame.math.Vector2(1, 1)


        self.x_0 = 0
        self.y_0 = 0
        self.vx_0 = [np.random.uniform(0.1, 50.0), np.random.uniform(0.1, 50.0)]
        self.vy_0 = [np.random.uniform(0.1, 50.0), np.random.uniform(0.1, 50.0)]

    def draw(self, screen):
        self.screen = screen
        pygame.draw.circle(self.screen,(255,255,255),(self.x_0, self.y_0), self.radius)

    def update(self, dt):
        self.horizontal_movement(dt)
        self.vertical_movement(dt)

    def collision_check(self):
        collision_x = self.position.x - self.radius
        collision_y = self.position.y + self.radius
        return collision_x, collision_y

    def horizontal_movement(self, dt):
        #self.velocity.x += self.acceleration.x*dt
        #self.limit_velocity(4)
        #self.position.x += self.velocity.x * dt + (0.5 * self.acceleration.x ) * (dt*dt)
        self.position.x += self.velocity.x * dt
        x, y = self.collision_check()
        if x < 0 or WIDTH < x:
            self.x_0 =(-1)*self.position.x
        else:
            self.x_0 = self.position.x


    def vertical_movement(self, dt):
        #self.velocity.y += self.acceleration.y * dt
        #self.limit_velocity(4)
        #self.position.y += self.velocity.y * dt + (0.5 * self.acceleration.y) * (dt * dt)
        self.position.y += self.velocity.y * dt
        self.y_0 = self.position.y

    def limit_velocity(self, max_v):
        min(-max_v, max(self.velocity.x, max_v))
        if abs(self.velocity.x < 0.1):
            self.velocity = 0.0


    #def new_velocity(self):
     #   vx = vx + ax*t
     #   vy = vy + ay*t


circle1 = Circle_Object()

def redraw_window(screen):
    circle1.draw(screen)



def main():
    pygame.init()
    scaling = 0.00001
    dt = clock.tick(60) * scaling * FPS
    running = True


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        circle1.update(dt)
        redraw_window(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    quit()

if __name__ == '__main__':
    main()
