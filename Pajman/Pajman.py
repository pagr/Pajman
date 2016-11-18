import pygame
import sys
import Level
import Pacman

print sys.path[0]

pygame.init()

screen = pygame.display.set_mode((640, 480))
map = Level.Level(screen, 50, 50)
pacman = Pacman.Pacman(screen)
drawables = [map, pacman]
updatables = [pacman]

while(True):
    screen.fill((0,0,0))

    keys = pygame.key.get_pressed()
    for updatable in updatables:
        updatable.update(keys)

    for drawable in drawables:
        drawable.draw()


    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()