from settings import *
import pygame

class Bar:
    def __init__(self, height, width, hpos, color):
        self.pos = 0
        self.width = width
        self.hpos = hpos 
        self.height = height
        self.color = color
        self.delta = 0
        self.quickness = 17

    def up(self):
        self.delta = self.quickness * -1

    def down(self):
        self.delta = self.quickness
        
    def stop(self):
        self.delta = 0

    def move(self):
        self.pos += self.delta
        if self.pos > max_y - self.height: self.pos = max_y - self.height
        if self.pos < 0 : self.pos = 0

    def paint(self, game_display):
        pygame.draw.rect(game_display, self.color, [self.hpos, self.pos, self.width, self.height])
