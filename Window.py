import pygame
import asyncio
import sys

class Window:
    def __init__(self, two_dimensional_list_to_render, width,height):
        self.width = width
        self.height = height
        pygame.display.set_caption("Bomberman")
        self.two_dimensional_list_to_render = two_dimensional_list_to_render

    def update_screen(self):
        pygame.display.flip()
