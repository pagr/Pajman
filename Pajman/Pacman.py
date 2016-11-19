import pygame

class Pacman:
    def __init__(self, screen, map, player):
        self.screen = screen
        self.map = map
        self.pos = [int(map.stepx * 4.5), int(map.stepy * 4.5)]
        self.wanted_direction = 0
        self.current_direction = 0
        self.points = 0
        self.speedx = [0,1,-1,0,0]
        self.speedy = [0,0,0,-1,1]
        self.mouth_angle = 6.24
        self.mouth_opening = False
        self.player = player

    def draw(self):
        pacman = pygame.draw.arc(self.screen, (255, 255, 0), (self.pos[0] - self.map.stepx/2, self.pos[1] - self.map.stepy/2, self.map.stepx, self.map.stepy  ), 0, self.mouth_angle, self.map.stepx/2)

        font = pygame.font.Font(None, 26)
        text = font.render("score : " + str(self.points), 1, (0, 0, 0))
        textpos = text.get_rect()
        textpos.centerx = self.screen.get_rect().centerx/2*-(self.player*2-1) + self.screen.get_rect().centerx
        self.screen.blit(text, textpos)

    def update(self, keys):
        if self.player == 0:
            if keys[pygame.K_RIGHT]:
                self.wanted_direction = 1
            elif keys[pygame.K_LEFT]:
                self.wanted_direction = 2
            elif keys[pygame.K_UP]:
                self.wanted_direction = 3
            elif keys[pygame.K_DOWN]:
                self.wanted_direction = 4
        else:
            if keys[pygame.K_d]:
                self.wanted_direction = 1
            elif keys[pygame.K_a]:
                self.wanted_direction = 2
            elif keys[pygame.K_w]:
                self.wanted_direction = 3
            elif keys[pygame.K_s]:
                self.wanted_direction = 4
        
        self.pos[0] += self.speedx[self.current_direction] * 4
        self.pos[1] += self.speedy[self.current_direction] * 4

        if self.mouth_opening:
            self.mouth_angle += 0.2
            if self.mouth_angle > 6.10:
                self.mouth_opening = False
        else:
            self.mouth_angle -= 0.2
            if self.mouth_angle < 4.6:
                self.mouth_opening = True

        if self.pos[0] % self.map.stepx == self.map.stepx/2 and self.pos[1] % self.map.stepy == self.map.stepy/2:
            if (self.map.square_type(self.pos[0] + self.speedx[self.wanted_direction] * self.map.stepx, self.pos[1] + self.speedy[self.wanted_direction] * self.map.stepy ) == 1):
                self.current_direction = 0
            else:
                self.current_direction = self.wanted_direction

        if (self.map.square_type(self.pos[0], self.pos[1]) == 2 or self.map.square_type(self.pos[0], self.pos[1]) == 3):
            self.map.remove_dot(self.pos[0], self.pos[1])
            self.points += 1

    
  
