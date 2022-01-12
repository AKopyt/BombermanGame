import pygame

class  Player:
    def __init__(self,screen_resolution, screen_width,screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen_resolution = screen_resolution

        self.image = pygame.image.load('images/player.bmp')
        self.image =  pygame.transform.smoothscale(self.image, (self.screen_width, screen_height))
        self.rect = self.image.get_rect()




    def blitme(self):
        self.screen_resolution.blit(self.image, self.rect)

