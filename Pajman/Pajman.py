import pygame
import sys
import Level
import Pacman

print sys.path[0]

pygame.init()

WIDTH = 720
HEIGHT = 1280

screen = pygame.display.set_mode((HEIGHT, WIDTH))
map = Level.Level(screen, HEIGHT, WIDTH)
pacman = Pacman.Pacman(screen)

while(True):
    screen.fill((0,0,0))
    map.draw()
    pacman.draw()
    keys = pygame.key.get_pressed()
    pacman.update(keys)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()