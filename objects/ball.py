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
