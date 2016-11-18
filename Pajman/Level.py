import pygame

class Level:

    def __init__(self, screen, width, height):
        self.width = width
        self.height = height
        self.screen = screen
        #self.grid = 

    def draw(self):
        outer_wall_upper = pygame.draw.lines(self.screen, (255, 255, 255), False, [[0, self.height / 2 - 50],[50, self.height / 2 - 50], [50, 50], [self.width - 50, 50], [self.width - 50, self.height / 2 - 50], [1280, self.height / 2 - 50]], 5)
        other_wall_lower = pygame.draw.lines(self.screen, (255, 255, 255), False, [[0, self.height / 2 + 50],[50, self.height / 2 + 50], [50, self.height - 50], [self.width - 50, self.height - 50], [self.width - 50, self.height / 2 + 50], [1280, self.height / 2 + 50]], 5)
