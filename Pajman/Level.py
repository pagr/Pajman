import pygame

class Level:
    def __init__(self, screen, width, height):
        self.width = width
        self.height = height
        self.screen = screen

    def draw(self):
        rect = pygame.draw.rect(self.screen, (255, 255, 255), (0, 0, self.width, self.height))
 #       outer_wall = pygame.draw.lines(self.screen, (255, 255, 255), [(10, 50), (200, 200)], 5)
