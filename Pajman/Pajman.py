﻿import pygame
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


pacman = Pacman.Pacman(screen, map)
ghost = Ghost.Ghost(screen, map)

drawables = [map] + [pacman] + [ghost]
updatables = [pacman]
ghostmovables = [ghost]

while(True):
    screen.fill((0,0,0))
    
    keys = pygame.key.get_pressed()
    for updatable in updatables:
        updatable.update(keys)

    ghostKeys = random.randint(0,4)
    for ghostmovable in ghostmovables:
        ghostmovable.update(ghostKeys)

    for drawable in drawables:
        drawable.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()

    clock.tick(60)
