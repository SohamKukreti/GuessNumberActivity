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


def init():
    global offset, factor, screen
    global black, w, h, imgf, font
    screen = pygame.display.get_surface()
    pygame.display.set_caption("Number Guesser")
    w, h = screen.get_size()
    black = (0, 0, 0)
    if float(w) / float(h) > 1.5:
        offset = (w - 4 * h // 3) // 2
    else:
        h = int(.75 * w)
        offset = 0
    factor = float(h) / 24
    imgf = float(h) / 1000
    if pygame.font:
        t = int(70 * imgf)
        font = pygame.font.Font(None, t)
    global welcome, main, end
    welcome = True
    main = False
    end = False


def sx(f):  # scale x function
    return int(f * factor + offset + .5)


def sy(f):  # scale y function
    return int(f * factor + .5)
