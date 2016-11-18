import pygame

class Pacman:
    def __init__(self, screen, map):
        self.screen = screen
        self.map = map
        self.pos = [int(map.stepx * 4.5), int(map.stepy * 4.5)]
        self.wanted_direction = 0
        self.current_direction = 0
        self.points = 0
        self.speedx = [0,1,-1,0,0]
        self.speedy = [0,0,0,-1,1]

    def draw(self):
        pacman = pygame.draw.circle(self.screen, (255, 255, 0), (self.pos[0], self.pos[1]), self.map.stepx / 2 - 2)

    def update(self, keys):

        if keys[pygame.K_RIGHT]:
            self.wanted_direction = 1
        elif keys[pygame.K_LEFT]:
            self.wanted_direction = 2
        elif keys[pygame.K_UP]:
            self.wanted_direction = 3
        elif keys[pygame.K_DOWN]:
            self.wanted_direction = 4
        
        self.pos[0] += self.speedx[self.current_direction] * 4
        self.pos[1] += self.speedy[self.current_direction] * 4

        if self.pos[0] % self.map.stepx == self.map.stepx/2 and self.pos[1] % self.map.stepy == self.map.stepy/2:
            if (self.map.square_type(self.pos[0] + self.speedx[self.wanted_direction] * self.map.stepx, self.pos[1] + self.speedy[self.wanted_direction] * self.map.stepy ) == 1):
                self.current_direction = 0
            else:
                self.current_direction = self.wanted_direction

        if (self.map.square_type(self.pos[0], self.pos[1]) == 2 or self.map.square_type(self.pos[0], self.pos[1]) == 3):
            self.map.remove_dot(self.pos[0], self.pos[1])
            self.points += 1

    
  
