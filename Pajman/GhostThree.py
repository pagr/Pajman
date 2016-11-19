import pygame
import Moves

class GhostThree(Moves.Moves):
    """description of class"""

    def draw(self):
        ghost = pygame.draw.circle(self.screen, (18, 191, 47), (self.pos[0], self.pos[1]),  self.map.stepx / 2 - 2)
      
    def update(self, keys):
        self.wanted_direction = keys
        
        super(self.__class__,self).update(self.wanted_direction, True)
