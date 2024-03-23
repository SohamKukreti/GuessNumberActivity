import pygame
import g

class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * g.imgf, self.image.get_height() * g.imgf))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if not self.clicked:
                    self.clicked = True
                    return True
        if event.type == pygame.MOUSEBUTTONUP:
            self.clicked = False
        return False
