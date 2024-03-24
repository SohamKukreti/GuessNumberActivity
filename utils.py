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

import random
import pygame
import g

screen = pygame.display.get_surface()


def get_random_numbers(size, possible_number):
    i = 0
    array = []
    while i < size:
        x = random.randint(1, 100)
        if possible_number[x - 1]:
            if x not in array:
                array.append(x)
            i += 1
        ct = 0
        for elem in possible_number:
            if elem is False:
                ct += 1
        if ct == 100:
            break
    return array


def check_number(possible_number):
    count = 0
    for i in possible_number:
        if i is True:
            count += 1
    if (count == 2):
        return 'check'
    if (count == 1):
        return 'win'
    return 'play'


def check_loss(possible_number):
    for i in possible_number:
        if i is True:
            return False
    return True


def get_coordinates(numbers, width, height):
    x = width * 0.5
    y = height * 0.2
    coords = []
    for i in range(1, len(numbers)+1):
        coords.append((x, y))
        x += width * 0.0833
        if i == 5:
            x = width * 0.5
            y += width * 0.0625
    return coords


def text_blit(text, font, text_col, x, y):
    txt = font.render(text, True, text_col)
    g.screen.blit(txt, (x, y))
