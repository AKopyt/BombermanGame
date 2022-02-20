import pygame
import sys

class Window:
    def __init__(self, List_objects_to_render,two_dimensional_list_to_render, width,height):
        self.width = width
        self.height = height
        pygame.display.set_caption("Bomberman")
        self.Objects_to_render = List_objects_to_render
        self.two_dimensional_list_to_render = two_dimensional_list_to_render

    def update_screen(self):
        pygame.display.flip()
        for object in self.Objects_to_render:
            object.blitme()
        for sublist in self.two_dimensional_list_to_render:
            for square in sublist:
                if not square.check_if_square_is_empty():
                    square.object.blitme()
