#
# Copyright (C) 2024 Soham Kukreti
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
import sys
import utils
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from button import Button
import g


class Guess:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Guess the number")
        self.img = pygame.image.load("assets/wizard.png")
        self.size = 10
        self.possible_number = [True] * 100
        self.font = pygame.font.Font(None, 48)
        self.number_present = False
        self.numbers = []
        self.win_text = ''
        self.lose_text = ''
        pygame.mixer.init()
        self.click_sound = pygame.mixer.Sound('assets/clicksound.ogg')
        self.click_sound.set_volume(0.4)
        self.clock = pygame.time.Clock()
        self.game_state = "play"

    def display(self):
        self.screen = pygame.display.get_surface()
        self.screen.fill((145, 213, 226))
        self.img = pygame.transform.scale(self.img, (int(g.w* 0.5), int(g.h * 0.75)))
        self.screen.blit(self.img, (0, g.h - self.img.get_height()))
        if self.game_state == "play" or self.game_state == "check":
            self.yes_button.draw(self.screen)
            self.no_button.draw(self.screen)
            if self.game_state == "check":
                self.draw_text(f"Is your number : {self.numbers[0]}?", g.font, (0, 0, 0), g.sx(6), g.sy(0.8))
            else:
                self.draw_text("Is your number on the screen?", g.font, (0, 0, 0), g.sx(6), g.sy(0.8))
                coords = utils.get_coordinates(self.numbers, g.w, g.h)
                for i in range(0, len(coords)):
                    self.draw_text(str(self.numbers[i]), g.font, (0, 0, 0), coords[i][0], coords[i][1])
        elif self.game_state == "win":
            self.draw_text(self.win_text, g.font, (0, 0, 0), g.sx(5), g.sy(0.8))
        elif self.game_state == "lose":
            self.draw_text(self.lose_text, g.font, (0, 0, 0), g.sx(3), g.sy(0.8))
        pygame.display.update()

    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    def button_setup(self):
        self.screen = pygame.display.get_surface()
        yes_img = pygame.image.load('assets/Yes.png')
        no_img = pygame.image.load('assets/no.png')
        self.yes_button = Button(g.sx(15), g.sy(20), yes_img)
        self.no_button = Button(g.sx(23), g.sy(20), no_img)

    def game_logic(self):
        self.game_state = utils.check_number(self.possible_number)
        if utils.check_loss(self.possible_number):
            self.game_state = "lose"
        if not self.number_present and self.no_button.clicked == True:
            if self.game_state == "check":
                self.possible_number[self.numbers[0] - 1] = False
            else:
                for i in self.numbers:
                    self.possible_number[i - 1] = False
            self.no_button.clicked = False
            self.numbers = utils.get_random_numbers(self.size, self.possible_number)
        if self.number_present and self.yes_button.clicked:
            self.yes_button.clicked = False
            if self.game_state == "check":
                self.game_state = "win"
                self.possible_number[self.numbers[0] - 1] = False
            else:
                for i in range(0, 100):
                    self.possible_number[i] = False
                for num in self.numbers:
                    self.possible_number[num - 1] = True
                self.size = int(self.size / 2)
                self.numbers = utils.get_random_numbers(self.size, self.possible_number)

    def run(self):
        pygame.mixer.music.load('assets/theme.ogg')
        pygame.mixer.music.play(-1)
        g.init()
        going = True
        self.button_setup()
        self.numbers = utils.get_random_numbers(self.size, self.possible_number)
        while going:
            while Gtk.events_pending():
                Gtk.main_iteration()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    going = False
                if self.yes_button.check_click(event):
                    self.click_sound.play()
                    self.number_present = True
                if self.no_button.check_click(event):
                    self.click_sound.play()
                    self.number_present = False
            if self.game_state == "play" or self.game_state == "check":
                self.game_logic()
            elif self.game_state == "win":
                self.win_text = f"Your number is {self.numbers[0]}"
            elif self.game_state == "lose":
                self.lose_text = "I could not guess your number!"
            self.display()
            self.clock.tick(30)


if __name__ == "__main__":
    game = Guess()
    game.screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)
    game.run()
    pygame.quit()
    sys.exit()
