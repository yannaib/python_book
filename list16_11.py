import pygame, sys
me=49
pygame.init()
screen=pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball=pygame.image.load("beach_ball.png")
nothing=pygame.image.load("nothing.png")
screen.blit(my_ball,[me+1,50])
pygame.display.flip()
for i in range(450):
	pygame.time.delay(25)
	me+=1
	screen.blit(my_ball,[me+1,50])
	screen.blit(nothing,[me,50])
	pygame.display.flip()
while (True):
    for event in pygame.event.get ():
        if event.type==pygame.QUIT:
            sys.exit ()