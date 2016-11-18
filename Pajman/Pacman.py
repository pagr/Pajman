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
        elif keys[pygame.K_LEFT]:
                self.move_left()
        elif keys[pygame.K_UP]:
                self.move_up()
        elif keys[pygame.K_DOWN]:
                self.move_down()
     

    def move_right(self):
        for i in range(0,100):
            self.pos[0] += 1

    def move_left(self):
        for i in range(0,100):
            self.pos[0] -= 1

    def move_up(self):
         for i in range(0,100):
            self.pos[1] -= 1

    def move_down(self):
        for i in range(0,100):
            self.pos[1] += 1

  