import pygame
import Moves
class Pacman(Moves.Moves):
   
    def update(self, keys):

        if keys[pygame.K_RIGHT]:
            self.wanted_direction = 1
        elif keys[pygame.K_LEFT]:
            self.wanted_direction = 2
        elif keys[pygame.K_UP]:
            self.wanted_direction = 3
        elif keys[pygame.K_DOWN]:
            self.wanted_direction = 4
        
        super(self.__class__,self).update(keys, False)
  
