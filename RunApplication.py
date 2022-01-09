import pygame
from Player import Player
from Board  import Board
import sys



class Window:
    def __init__(self):
        pygame.init()
        self.screen_resolution = pygame.display.set_mode((500,500))
        pygame.display.set_caption("Bomberman")

    def run_game(self):
        while True:
            self.check_events()
            self.update_screen()

    def update_screen(self):
        pygame.display.flip()


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


#NaszeOkno = Window()
#NaszeOkno.run_game()
plansza = Board()
gracz = Player(plansza)

