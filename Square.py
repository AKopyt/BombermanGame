import pygame
from DrawAbstract import DrawAbstract

class Square:
    def __init__(self, settings,x,y):
        self.square_width = settings.width/settings.amount_of_squares
        self.square_height = settings.height/settings.amount_of_squares
        self.posX= x * self.square_width
        self.posY = y * self.square_height
        self.left_up_corner=[self.posX,self.posY]
        self.right_up_corner = [self.posX+self.square_width, self.posY]
        self.left_down_corner = [self.posX, self.posY+ self.square_height]
        self.right_down_corner = [self.posX+self.square_width, self.posY+self.square_height]
        self.object = None

    def check_if_square_is_empty(self):
        if self.object is None:
            return True
        else:
            return False

    def put_the_object(self,object):
        object.rect.x = self.left_up_corner[0]
        object.rect.y = self.left_up_corner[1]
        self.object = object






