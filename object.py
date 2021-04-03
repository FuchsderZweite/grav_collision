import pygame
from random import randint
id_list = []

WIDTH_FIELD = 600
HEIGHT_FIELD = 600
VELOCITY_MAX = 13

class Circle:
    def __init__(self):
        self.id_list = id_list
        self.id = len(self.id_list) + 1
        self.id_list.append(self.id)
        self.mass = randint(10, 100)
        self.radius = randint(10, 40)
        self.pos = pygame.math.Vector2(randint(0+self.radius, WIDTH_FIELD-self.radius), randint(0+self.radius, HEIGHT_FIELD-self.radius))
        self.v = pygame.math.Vector2(randint(-VELOCITY_MAX, VELOCITY_MAX), randint(-VELOCITY_MAX, VELOCITY_MAX))
        if self.v.x == 0 or self.v.y == 0:
            self.v = pygame.math.Vector2(randint(-VELOCITY_MAX, VELOCITY_MAX), randint(-VELOCITY_MAX, VELOCITY_MAX))
        #self.a = pygame.math.Vector2(1, 1)
        self.color = (randint(0,255),randint(0,255),randint(0,255))

        # self.gravity = 0.35
        # self.friction = -0.12

    def draw(self, screen):
        self.screen = screen
        pygame.draw.circle(self.screen, self.color, (self.pos.x, self.pos.y), self.radius)

    def update(self, dt):
        self.horizontal_movement(dt)
        self.vertical_movement(dt)


    def intersect(self):
        pass

    def check_wall_collision(self):
        pass


    def horizontal_movement(self, dt):
        #self.velocity.x += self.acceleration.x*dt
        #self.limit_velocity(4)
        #self.position.x += self.velocity.x * dt + (0.5 * self.acceleration.x ) * (dt*dt)
        self.pos.x += self.v.x * dt
        col_left, col_right, col_top, col_bottom = self.collision_check()
        if col_left or col_right:
            self.v.x *= -1



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
        elif self.pos.x + self.radius >= WIDTH_FIELD:
            collision_right = True
        elif self.pos.y - self.radius <= 0.0:
            collision_top = True
        elif self.pos.y + self.radius >= HEIGHT_FIELD:
            collision_bottom = True
        return collision_left, collision_right, collision_top, collision_bottom


    def circle_collision(self):
        distance_x = self.pos.x
        distance_y = 2
        pass

    def add_text(self):
        self.screen.blit(self.font.render('Hello!', True, (255, 0, 0)), (200, 100))
        pygame.display.update()



class Table():
    def __init__(self):
        self.WIDTH = 900
        self.HEIGHT = 600



class Window():
    def __init__(self):
        self.WIDTH = 900
        self.HEIGHT = 600