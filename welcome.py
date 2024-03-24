#
# Copyright (c) 2024 Soham Kukreti
#
# This program is free software; you can redistribute it
# and/or modify it under the terms of the GNU General
# Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at
# your option) any later version.
#
# This program is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even
# the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.
#
# You should have received a copy of the GNU General
# Public License along with this program; if not,
# write to the Free Software Foundation, Inc.,
# 51 Franklin St, Fifth Floor, Boston, MA
# 02110-1301  USA
#

import pygame
import button
import g
import utils


class Welcome:
    def __init__(self):
        yes_img = pygame.image.load('assets/play.png')
        self.play_button = button.Button(g.sx(13), g.sy(20), yes_img)

    def draw(self):
        g.screen.fill((145, 213, 226))
        utils.text_blit("Welcome To Number Guesser Activity!",
                        g.font, g.black, g.sx(5), g.sy(10))
        utils.text_blit("Think of any number between 1 and 100!",
                        g.font, g.black, g.sx(5), g.sy(15))
        self.play_button.draw(g.screen)
