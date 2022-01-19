import pygame

class Board:
    def __init__(self, screen, screen_width, screen_height):
        self.board_width = screen_width
        self.board_height = screen_height
        self.screen = screen

        self.image = pygame.image.load('images/background.jpeg')
        self.image = pygame.transform.smoothscale(self.image, (self.board_width, self.board_height))
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)