import pygame
import sys

class Window:
    def __init__(self, List_objects_to_render, width,height):
        self.width = width
        self.height = height
        pygame.display.set_caption("Bomberman")
        self.Objects_to_render = List_objects_to_render

    def run_game(self):
        while True:
            self.check_events()
            self.update_screen()

    def update_screen(self):
        pygame.display.flip()
        for object in self.Objects_to_render:
            object.blitme()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()