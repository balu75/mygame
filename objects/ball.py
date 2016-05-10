from colors import *
from settings import *

import pygame

class Ball:
    def __init__(self, height, width, x, y, delta_x, delta_y):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.delta_x = delta_x
        self.delta_y = delta_y

    def move(self):
        self.x += self.delta_x
        self.y += self.delta_y


        if self.y > max_y-self.height or self.y - self.height < 0:
            self.delta_y *= -1

    def paint(self, game_display):
        pygame.draw.circle(game_display, green, [self.x, self.y], self.width)
