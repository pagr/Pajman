import pygame

class Pacman:
    def __init__(self, screen):
        self.screen = screen
        self.pos = [100, 100]

    def draw(self):
        pacman = pygame.draw.circle(self.screen, (255, 255, 0), (self.pos[0], self.pos[1]), 40)

    def update(self, keys):
        if keys[pygame.K_RIGHT]:
            self.move_right()
        if keys[pygame.K_LEFT]:
            self.move_left()
        if keys[pygame.K_UP]:
            self.move_up()
        if keys[pygame.K_DOWN]:
            self.move_down()

    def move_right(self):
        self.pos[0] += 1

    def move_left(self):
        self.pos[0] -= 1

    def move_up(self):
        self.pos[1] -= 1

    def move_down(self):
        self.pos[1] += 1