import pygame
import Moves

class GhostTwo(Moves.Moves):
    """description of class"""
    def draw(self):
       ghost = pygame.draw.circle(self.screen, (24, 18, 191), (self.pos[0], self.pos[1]),  self.map.stepx / 2 - 2)
      
    def update(self, keys):
       self.wanted_direction = keys
        
       super(self.__class__,self).update(self.wanted_direction, True)

