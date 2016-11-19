import pygame
import sys
import Level
import Pacman
import Dot
import Ghost
import random

pygame.init()

WIDTH = 360
HEIGHT = 640


clock = pygame.time.Clock()
screen = pygame.display.set_mode((HEIGHT, WIDTH))
map = Level.Level(screen, HEIGHT, WIDTH)


pacmanA = Pacman.Pacman(screen, map,0)
pacmanB = Pacman.Pacman(screen, map,1)
ghost = Ghost.Ghost(screen, map)

drawables = [map] + [pacmanA, pacmanB] + [ghost]
updatables = [pacmanA, pacmanB]
ghostmovables = [ghost]
b1 = 0

while(True):
    screen.fill((0,0,0))
    
    keys = pygame.key.get_pressed()
    for updatable in updatables:
        updatable.update(keys)

    ghostkeys = random.randint(0,4)
    for ghostmovable in ghostmovables:
        ghostmovable.update(ghostkeys)

    for drawable in drawables:
        drawable.draw()

    oldb = b1
    b1,b2,b3 = pygame.mouse.get_pressed()
    x,y = pygame.mouse.get_pos()
 
    if b1 != oldb and b1 == 1:
        map.grid[x/map.stepx][y/map.stepy] = 0
        oldb = b1
    if b3:
        map.save()
 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()

    clock.tick(60)
