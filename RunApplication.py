from Window import Window
from Player import Player
from Board import Board
from Settings import Settings
import sys
import pygame
from DrawAbstract import DrawAbstract
from Bomb import Bomb
from Square import Square
import asyncio

class RunAplication:
    def __init__(self, settings, gracz: DrawAbstract, board: DrawAbstract):

        pygame.init()

        self.settings = settings
        self.player = gracz
        self.board = board
        self.two_dimensional_list = self.make_two_dimensional_array(self.settings)
        self.board.blitme()
        #self.lista = []
        #self.lista.append(self.board)

        self.NaszeOkno = Window(self.two_dimensional_list,self.settings.width, self.settings.height)

    def run_game(self):

        while True:
            self.player.update()
            self.player.blitme()

            self.NaszeOkno.update_screen()
            self.check_events()

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
        bomb = Bomb(self.settings,self.player.send_x_coord(), self.player.send_y_coord())
        self.try_to_put_object_inside_square(bomb,self.player.send_x_coord(),self.player.send_y_coord())
        for sublist in self.two_dimensional_list:
            for square in sublist:
                if not square.check_if_square_is_empty():
                    square.object.blitme()

    def make_two_dimensional_array(self, settings):
        listX=[]

        for x in range(settings.amount_of_squares):
            listY = []
            for y in range(settings.amount_of_squares):
                listY.append(Square(settings,x,y))
            listX.append(listY)
        return listX

    def try_to_put_object_inside_square(self,object,x,y):
        for sublist in self.two_dimensional_list:
            for square in sublist:
                 if square.left_up_corner[0] <= x and x<square.right_up_corner[0]:
                     if square.left_up_corner[1] <= y and y<= square.left_down_corner[1]:
                         if square.check_if_square_is_empty():
                             square.put_the_object(object)

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

    def run(self):
        self.app.run_game()

config= Config()
config.run()


