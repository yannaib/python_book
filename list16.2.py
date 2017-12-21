import pygame, sys
pygame.init ()
screen=pygame.display.set_mode ([640,480])
screen.fill([63,63,63])
pygame.draw.circle(screen,[0,191,0],[320,240],30,0)
pygame.display.flip()
while (True):
    for event in pygame.event.get ():
        if event.type==pygame.QUIT:
            sys.exit ()
