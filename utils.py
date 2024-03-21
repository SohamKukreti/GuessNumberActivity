#
# Copyright (c) 2024 Soham Kukreti
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import random
import pygame

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
            if elem == False:
                ct+=1
        if ct == 100:
            break

    return array

def check_number(possible_number):
    count = 0
    for i in possible_number:
        if i == True:
            count += 1
    if(count == 2):
         return 'check'
    if(count == 1):
         return 'win'
    return 'play'

def check_loss(possible_number):
    for i in possible_number:
        if i == True:
            return False
    return True