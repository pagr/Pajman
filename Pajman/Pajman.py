import pygame
import sys
import Level
import Pacman
import Dot
import Ghost

pygame.init()

WIDTH = 360
HEIGHT = 640


clock = pygame.time.Clock()
screen = pygame.display.set_mode((HEIGHT, WIDTH))
map = Level.Level(screen, HEIGHT, WIDTH)


pacman = Pacman.Pacman(screen, map)
ghost = Ghost.Ghost(screen, map)

drawables = [map] + [pacman] + [ghost]
updatables = [pacman]
b1 = 0

while(True):
    screen.fill((0,0,0))
    
    keys = pygame.key.get_pressed()
    for updatable in updatables:
        updatable.update(keys)

    for drawable in drawables:
        drawable.draw()

    oldb = b1
    b1,b2,b3 = pygame.mouse.get_pressed()
    x,y = pygame.mouse.get_pos()
 
    if b1 != oldb and b1 == 1:
        map.grid[x/map.stepx][y/map.stepy] = (map.grid[x/map.stepx][y/map.stepy] + 1) % 4
        oldb = b1
    if b3:
        map.save()
 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()

    clock.tick(60)
