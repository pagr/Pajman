import pygame

class Pacman:
    def __init__(self, screen, map):
        self.screen = screen
        self.pos = [100, 100]
        self.map = map

    def draw(self):
        pacman = pygame.draw.circle(self.screen, (255, 255, 0), (self.pos[0], self.pos[1]), 20)

    def update(self, keys):
        posx = self.pos[0]
        posy = self.pos[1]
        if keys[pygame.K_RIGHT]:
            self.move_right()
        elif keys[pygame.K_LEFT]:
            self.move_left()
        elif keys[pygame.K_UP]:
            self.move_up()
        elif keys[pygame.K_DOWN]:
            self.move_down()
        if (self.map.square_type(self.pos[0], self.pos[1]) == 1):
            self.pos[0] = posx
            self.pos[1] = posy
        if (self.map.square_type(self.pos[0], self.pos[1]) == 2 or self.map.square_type(self.pos[0], self.pos[1]) == 3):
            self.map.remove_dot(self.pos[0], self.pos[1])     

    def move_right(self):
        self.pos[0] += 40

    def move_left(self):
        self.pos[0] -= 40

    def move_up(self):
        self.pos[1] -= 40

    def move_down(self):
        self.pos[1] += 40

    def move_change(self):
        self.pos[0] = self.pos[0]