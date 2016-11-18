import pygame

class Dot(object):
    """description of class"""

    def __init__(self,screen,x,y):
        self.x = x
        self.y = y
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen, (255,255,255), (self.x, self.y), 10)


        
