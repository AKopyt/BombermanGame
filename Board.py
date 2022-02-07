import pygame
from DrawAbstract import DrawAbstract

class Board(DrawAbstract):
    def __init__(self, settings):
        self.screen = settings.screen
        self.settings = settings

        self.image = pygame.image.load('images/background.jpeg')
        self.image = pygame.transform.smoothscale(self.image, (self.settings.board_width, self.settings.board_height))
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)