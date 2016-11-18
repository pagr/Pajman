import pygame
import sys
import Level
import Pacman
import Dot

pygame.init()

WIDTH = 360
HEIGHT = 640


clock = pygame.time.Clock()
screen = pygame.display.set_mode((HEIGHT, WIDTH))
map = Level.Level(screen, HEIGHT, WIDTH)


pacman = Pacman.Pacman(screen, map)

drawables = [map] +[pacman]
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
    clock.tick(60)
