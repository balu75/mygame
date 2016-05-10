#!/usr/bin/python3

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

import pygame
from colors import white, black, red, green
from settings import max_x, max_y
from objects.bar import Bar
from objects.ball import Ball

def init():
    lbar = Bar(50, 10, 0, red)
    rbar = Bar(30, 10, max_x - 10, black)
    a_ball = Ball(15, 15, int(max_x/2), int(max_y/2), -5, 1)

    objects = [lbar, rbar, a_ball]

    return (lbar, rbar, a_ball, objects)

(lbar, rbar, a_ball, objects) = init()

# game logic
pygame.init()

game_display = pygame.display.set_mode((max_x, max_y))

pygame.display.set_caption("mygame 0.01")

pygame.display.update()

game_exit = False

clock = pygame.time.Clock()

while not game_exit:
    game_display.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == 113:
                lbar.up()
            if event.key == 97:
                lbar.down()
            if event.key == 252:
                rbar.up()
            if event.key == 228:
                rbar.down()
            if event.unicode == "Q":
                game_exit = True
            if event.unicode == "R":
                (lbar, rbar, a_ball, objects) = init()

        if event.type == pygame.KEYUP:
            if event.key == 113 or event.key == 97:
                lbar.stop()
            if event.key == 252 or event.key == 228:
                rbar.stop()

            #print(event)


    # collision check ball with left bar
    #print("ball.x="+str(a_ball.x)+"lbar.width="+str(lbar.width))
    
    if a_ball.x-a_ball.width == lbar.width:
        if a_ball.y >= lbar.pos and a_ball.y <= lbar.pos + lbar.height:
            # bounce ball
            #print("bounce...")
            a_ball.delta_x *= -1

    if a_ball.x+a_ball.width == max_x - rbar.width:
        if a_ball.y >= rbar.pos and a_ball.y <= rbar.pos + rbar.height:
            # bounce ball
            #print("bounce...")
            a_ball.delta_x *= -1

    # collision check ball with border
    if a_ball.x - a_ball.width  <= 0:
        # game over
        game_exit = True

    if a_ball.x >= max_x :
        # game over
        game_exit = True
    
    for obj in objects:
        obj.move()

    for obj in objects:
        obj.paint(game_display)

    pygame.display.update()

    clock.tick(40)

pygame.quit()

quit()
