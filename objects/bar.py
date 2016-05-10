# Copyright (C) 2016
# Author: Thomas Gies <thomas.gies@gmx.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
