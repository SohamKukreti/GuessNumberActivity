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
        utils.text_blit("Welcome To Number Guesser Activity!", g.font, (0,0,0), g.sx(5), g.sy(10))
        utils.text_blit("Think of any number between 1 and 100!", g.font, (0,0,0), g.sx(5), g.sy(15))
        self.play_button.draw(g.screen)
    