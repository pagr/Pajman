import pygame
import Moves
import random

class Ghost(Moves.Moves):

    def __init__(self, screen, map, color):
        self.screen = screen
        self.map = map
        self.pos = [int(map.stepx * 4.5), int(map.stepy * 4.5)]
        self.wanted_direction = 0
        self.current_direction = 1
        self.points = 0
        self.speedx = [0,1,-1,0,0]
        self.speedy = [0,0,0,-1,1]
        self.color = color
      
    def draw(self):
         pacman = pygame.draw.circle(self.screen, self.color, (self.pos[0], self.pos[1]), self.map.stepx / 2 - 2)

    def update(self, keys):
        self.pos[0] += self.speedx[self.current_direction] * 4
        self.pos[1] += self.speedy[self.current_direction] * 4

        if self.pos[0] % self.map.stepx == self.map.stepx/2 and self.pos[1] % self.map.stepy == self.map.stepy/2:
            if random.randint(0,4) == 0:
                self.wanted_direction = random.randint(1,4)
            if (self.map.square_type(self.pos[0] + self.speedx[self.wanted_direction] * self.map.stepx, self.pos[1] + self.speedy[self.wanted_direction] * self.map.stepy ) == 1):
                self.current_direction = 0
                self.wanted_direction = random.randint(1,4)
            else:
                self.current_direction = self.wanted_direction



