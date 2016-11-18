import pygame
import random
class Level:
    def __init__(self, screen, width, height):
        self.width = width
        self.height = height
        self.screen = screen

        self.grid =  [[random.randint(0,2) for x in range(18)] for y in range(32)]  
        self.countx = len(self.grid)
        self.county = len(self.grid[0]) 
        self.stepx = self.width / self.countx 
        self.stepy = self.height / self.county
        
        self.grid[3][4] = 3
        self.grid[7][4] = 3
        self.grid[12][15] = 3

        for x in range(0, self.countx):
            self.grid[x][0] = 1
            self.grid[x][self.county-1] = 1

        for y in range(0, self.county):
            self.grid[0][y] = 1
            self.grid[self.countx-1][y] = 1

    def square_type(self, x, y):
        return self.grid[ int(x/self.stepx)][int(y/self.stepy)]

    def remove_dot(self, x, y):
        self.grid[int(x/self.stepx)][int(y/self.stepy)] = 0

    def draw(self):
        
        for x in range(0, self.countx):     
            for y in range(0, self.county): 
                if (self.grid[x][y] == 1):
                    pygame.draw.rect(self.screen, (255,255,255), (int(x*self.stepx), int(y*self.stepy), self.stepx, self.stepy))    
                elif (self.grid[x][y] == 2):     
                    pygame.draw.circle(self.screen, (255,255,0), (int(x*self.stepx+self.stepx/2), int(y*self.stepy+self.stepy/2)), 3)
                elif (self.grid[x][y] == 3):     
                    pygame.draw.circle(self.screen, (255,255,0),(int(x*self.stepx+self.stepx/2), int(y*self.stepy+self.stepy/2)), 5)

