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



ghost = Ghost.Ghost(screen, map, (170,20,20))
ghosttwo = Ghost.Ghost(screen, map, (170,84,236))
ghostthree = Ghost.Ghost(screen, map, (18,191,47))
ghostfour = Ghost.Ghost(screen, map, (255,18,191))
pacmanA = Pacman.Pacman(screen, map,0,[ghost, ghosttwo, ghostthree, ghostfour])
pacmanB = Pacman.Pacman(screen, map,1,[ghost, ghosttwo, ghostthree, ghostfour])

drawables = [map, ghost, ghosttwo, ghostthree, ghostfour, pacmanA, pacmanB]
updatables = [pacmanA, pacmanB, ghost, ghosttwo, ghostthree, ghostfour]
b1 = 0

while(True):
    screen.fill((0,0,0))
    
    for drawable in drawables:
        drawable.draw()

    keys = pygame.key.get_pressed()
    for updatable in updatables:
        updatable.update(keys)
   

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

    if (pacmanA.color == (255,0,0) and pacmanB.color == (255,0,0)):
        showEnd()
    count = 0
    for row in map.grid:
        for thing in row:
            if thing == 2:
                count+=1
    if count == 0:
        showEnd()

    clock.tick(60)

    def showEnd():
        while(1):
            font = pygame.font.Font(None, 40)

            text = font.render("Game Over" , 1, (0, 0, 0))
            textpos = text.get_rect()
            textpos.centerx = screen.get_rect().centerx
            textpos.centery = screen.get_rect().centery
            pygame.draw.rect(screen, (255,255,255),(100,100,HEIGHT-200,WIDTH-200))
            screen.blit(text, textpos)
            pygame.display.flip()