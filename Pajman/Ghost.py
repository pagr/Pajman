import pygame

class Ghost(object):
    """description of class"""

    def __init__(self, screen, map):
        self.screen = screen
        self.pos = [300, 300]
        self.map = map
        self.state = 0
        self.dist = 40
        self.xMove = 0
        self.yMove = 0
        self.direction = 1
        self.nextdirection = 3
        self.xdirection = [0,-self.dist,self.dist,0,0]
        self.ydirection = [0,0,0,-self.dist,self.dist]

    def draw(self):
        ghost = pygame.draw.circle(self.screen, (170, 20, 20), (self.pos[0], self.pos[1]), 20)
      
    def update(self):
        posx = self.pos[0]
        posy = self.pos[1]
        self.xMove = self.xdirection[self.nextdirection]
        self.yMove = self.ydirection[self.nextdirection]
        self.rect.move_ip[self.xMove, self.yMove]

        if (self.map.square_type(self.pos[0], self.pos[1]) == 1):
            self.pos[0] = posx
            self.pos[1] = posy
        else:
            self.direction = self.nextdirection
            self.nextdirection = randint(3,4)
      
           




