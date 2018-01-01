import pygame,sys,math
white=255
pygame.init ()
screen=pygame.display.set_mode ([640,480])
screen.fill([white,white,white])
plotPoints=[]
for x in range (0,640):
	y=int(math.sin(x/640.0*4*math.pi)*200+240)
	plotPoints.append([x,y])
pygame.draw.lines(screen,[0,0,0],False,plotPoints,1)
pygame.display.flip()
while (True):
    for event in pygame.event.get ():
        if event.type==pygame.QUIT:
            sys.exit ()