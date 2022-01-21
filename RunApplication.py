from Window import Window
from Player import Player
from Board import Board
from Settings import Settings
import sys
import pygame

class RunAplication:
    def __init__(self):
        self.width = 500
        self.height = 500
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.init()

        self.settings = Settings()
        self.player = Player(self.screen, self.width, self.height,self.settings)
        self.board = Board(self.screen, self.width, self.height)

        self.lista = []
        self.lista.append(self.board)
        self.lista.append(self.player)

        self.NaszeOkno = Window(self.lista, self.width, self.height)

    def run_game(self):
        while True:
            self.check_events()
            self.player.update()
            self.NaszeOkno.update_screen()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.player.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.player.moving_left = True
                if event.key == pygame.K_UP:
                    self.player.moving_up = True
                if event.key == pygame.K_DOWN:
                    self.player.moving_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.player.moving_left = False
                if event.key == pygame.K_UP:
                    self.player.moving_up = False
                if event.key == pygame.K_DOWN:
                    self.player.moving_down = False

rn = RunAplication()
rn.run_game()


