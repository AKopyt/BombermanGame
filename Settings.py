import pygame

class Settings:
    def __init__(self):
        self.player_speed = 1.5
        self.width = 500
        self.height = 500
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.board_width = self.width
        self.board_height = self.height
        self.Bomb_image = pygame.image.load("images/bomb1.png")
