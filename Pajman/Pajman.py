import pygame
import sys
import Level
import Pacman
import Dot

print sys.path[0]

pygame.init()

WIDTH = 720
HEIGHT = 1280


clock = pygame.time.Clock()
screen = pygame.display.set_mode((HEIGHT, WIDTH))
map = Level.Level(screen, HEIGHT, WIDTH)

dots = []

pacman = Pacman.Pacman(screen)
for i in range(0,10):
    dots.append(Dot.Dot(screen, i*146 % 500, i*10))

drawables = [map] + dots +[pacman]
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