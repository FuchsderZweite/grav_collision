import pygame
import numpy as np
from random import randint


WIDTH_FIELD = 600
HEIGHT_FIELD = 600
VELOCITY_MAX = 10

class Circle:
    def __init__(self):
        self.id_list = []
        self.id = len(self.id_list) + 1
        self.id_list.append(self.id)
        self.mass = randint(10, 100)
        self.radius = randint(10, 40)
        self.px, self.py = pygame.math.Vector2(randint(0+self.radius, WIDTH_FIELD-self.radius), randint(0+self.radius, HEIGHT_FIELD-self.radius))
        self.vx, self.vy = pygame.math.Vector2(randint(-VELOCITY_MAX, VELOCITY_MAX), randint(-VELOCITY_MAX, VELOCITY_MAX))
        if self.vx == 0 or self.vy == 0:
            self.v = pygame.math.Vector2(randint(-VELOCITY_MAX, VELOCITY_MAX), randint(-VELOCITY_MAX, VELOCITY_MAX))
        self.ax, self.ay = pygame.math.Vector2(1, 1)
        self.color = (randint(10,255),randint(10,255),randint(10,255))

        # self.gravity = 0.35
        # self.friction = -0.12



    def draw(self, screen):
        self.screen = screen
        circle_border = pygame.draw.circle(self.screen, (0,0,0), (self.px, self.py), self.radius, width=0)
        circle_fill = pygame.draw.circle(self.screen, self.color, (self.px, self.py), self.radius)
        return circle_fill, circle_border

    def update(self, dt):
        self.horizontal_movement(dt)
        self.vertical_movement(dt)


    def horizontal_movement(self, dt):
        self.px += self.vx * dt
        col_left, col_right, col_top, col_bottom = self.collision_check()
        if col_left or col_right:
            self.vx *= -1

    def vertical_movement(self, dt):
        self.py += self.vy * dt
        col_left, col_right, col_top, col_bottom = self.collision_check()
        if col_top or col_bottom:
            self.vy *= -1

    def limit_velocity(self, max_v):
        min(-max_v, max(self.vx, max_v))
        if abs(self.vx < 0.1):
            self.vx = 0.0
            self.vy = 0.0


    def collision_check(self):
        collision_left =  False
        collision_right = False
        collision_top = False
        collision_bottom = False

        if self.px - self.radius <= 0.0:
            collision_left = True
        elif self.px + self.radius >= WIDTH_FIELD:
            collision_right = True
        elif self.py - self.radius <= 0.0:
            collision_top = True
        elif self.py + self.radius >= HEIGHT_FIELD:
            collision_bottom = True
        return collision_left, collision_right, collision_top, collision_bottom

