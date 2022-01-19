import pygame

class  Player:
    def __init__(self,screen, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = screen

        self.image = pygame.image.load('images/player.png')
        self.image = pygame.transform.smoothscale(self.image, (self.screen_width*0.1, self.screen_height*0.1))
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

