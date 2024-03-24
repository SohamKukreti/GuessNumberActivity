#g.py globals
import pygame

def init():
    global offset, factor
    global screen, w, h, imgf, font
    screen = pygame.display.get_surface()
    pygame.display.set_caption("Number Guesser")
    w, h = screen.get_size() 
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
