from Window import Window
from Player import Player
import pygame

class RunAplication:
    def __init__(self):
        self.width = 500
        self.height = 500
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.init()

        self.player = Player(self.screen, self.width, self.height)
        self.lista = []
        self.lista.append(self.player)

        self.NaszeOkno = Window(self.lista, self.width, self.height)
        self.NaszeOkno.run_game()

rn = RunAplication()


