import pygame, sys, random
white=63
pygame.init ()
screen=pygame.display.set_mode ([640,480])
screen.fill([white,white,white])
for i in range (1):
	width=random.randint (0,250)
	height=random.randint (0,100)
	top=random.randint (0,400)
	left=random.randint (0,500)
	red=random.randint (0, 255)
	green=random.randint (0, 255)
	blue=random.randint (0, 255)
	pygame.draw.rect (screen, [red, green, blue], [left, top, width, height], 3)
pygame.display.flip()
'''
pygame.draw.circle(screen,[0,191,0], [ 320, 240], 30)
rect_color=[255,255,255]
rect_list=(250,150,300,200)
pygame.draw.rect(screen, rect_color, rect_list, 0)
pygame.display.flip()
'''
while (True):
    for event in pygame.event.get ():
        if event.type==pygame.QUIT:
            sys.exit ()
		#elif event.type==pygame. 
