import pygame
from DrawAbstract import DrawAbstract

class Bomb(DrawAbstract):
    def __init__(self, settings, x, y):
        self.screen_width = settings.width
        self.screen_height = settings.height
        self.screen = settings.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings

        self.image = self.settings.Bomb_image
        self.image = pygame.transform.smoothscale(self.image, (self.screen_width * 0.1, self.screen_height * 0.1))
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

