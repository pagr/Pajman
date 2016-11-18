import pygame

class Pacman:
    def __init__(self, screen, map):
        self.screen = screen
        self.pos = [100, 100]
        self.map = map
        self.wanted_direction = 0
        self.current_direction = 0

    def draw(self):
        pacman = pygame.draw.circle(self.screen, (255, 255, 0), (self.pos[0], self.pos[1]), 20)

    def update(self, keys):
        posx = self.pos[0]
        posy = self.pos[1]
        if keys[pygame.K_RIGHT]:
            wanted_direction = 1
        elif keys[pygame.K_LEFT]:
            wanted_direction = 2
        elif keys[pygame.K_UP]:
            wanted_direction = 3
        elif keys[pygame.K_DOWN]:
            wanted_direction = 4
        
        if current_direction == 1:
            move_right()
        elif current_direction == 2:
            move_left()
        elif current_direction == 3:
            move_up()
        elif current_direction == 4:
            move_down()

        if (self.map.square_type(self.pos[0], self.pos[1]) == 1):
            self.pos[0] = posx
            self.pos[1] = posy
        if posx % self.map.stepx == 0 and posy % self.map.stepy:
            current_direction = wanted_direction

        if (self.map.square_type(self.pos[0], self.pos[1]) == 2 or self.map.square_type(self.pos[0], self.pos[1]) == 3):
            self.map.remove_dot(self.pos[0], self.pos[1])     

    def move_right(self):
        self.pos[0] += 1

    def move_left(self):
        self.pos[0] -= 1

    def move_up(self):
        self.pos[1] -= 1

    def move_down(self):
        self.pos[1] += 1

  