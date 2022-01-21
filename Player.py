import pygame

class  Player:
    def __init__(self,screen, screen_width, screen_height,settings):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('images/player.png')
        self.image = pygame.transform.smoothscale(self.image, (self.screen_width*0.1, self.screen_height*0.1))
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right:
            self.x += self.settings.player_speed
        if self.moving_left:
            self.x -= self.settings.player_speed
        if self.moving_up:
            self.y -= self.settings.player_speed
        if self.moving_down:
            self.y += self.settings.player_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

