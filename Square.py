import pygame

class Square:
    def __init__(self, settings,x,y):
        self.square_width = settings.width/settings.amount_of_squares
        self.square_height = settings.height/settings.amount_of_squares
        self.posX= x * self.square_width
        self.posY = y * self.square_height
        self.left_up_corner=(self.posX,self.posY)
        self.right_up_corner = (self.posX+self.square_width, self.posY)
        self.left_down_corner = (self.posX, self.posY+ self.square_height)
        self.right_down_corner = (self.posX+self.square_width, self.posY+self.square_height)



