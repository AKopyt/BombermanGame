from Window import Window
from Player import Player
from Board import Board
from Settings import Settings
import sys
import pygame
from DrawAbstract import DrawAbstract
from Bomb import Bomb

class RunAplication:
    def __init__(self, settings, gracz: DrawAbstract, board: DrawAbstract):

        pygame.init()

        self.settings = settings
        self.player = gracz
        self.board = board

        self.lista = []
        self.lista.append(self.board)
        self.lista.append(self.player)

        self.NaszeOkno = Window(self.lista, self.settings.width, self.settings.height)

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
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

    def check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = True
        if event.key == pygame.K_LEFT:
            self.player.moving_left = True
        if event.key == pygame.K_UP:
            self.player.moving_up = True
        if event.key == pygame.K_DOWN:
            self.player.moving_down = True
        if event.key == pygame.K_b:
            self.drop_bomb()
        if event.key == pygame.K_q:
            sys.exit()

    def drop_bomb(self):
        bomb = Bomb(self.settings,self.player.x, self.player.y)
        self.lista.append(bomb)

    def check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
        if event.key == pygame.K_LEFT:
            self.player.moving_left = False
        if event.key == pygame.K_UP:
            self.player.moving_up = False
        if event.key == pygame.K_DOWN:
            self.player.moving_down = False

class Config:
    def __init__(self):
        self.settings = Settings()
        self.player = Player(self.settings.screen, self.settings.width, self.settings.height, self.settings)
        self.board = Board(self.settings)



        self.app = RunAplication(self.settings,self.player,self.board)

    def  run(self):
        self.app.run_game()



config= Config()
config.run()


