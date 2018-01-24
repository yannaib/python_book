import pygame,sys,random
pygame.init ()
screen=pygame.display.set_mode ([640,480])
screen.fill([255,255,255])
#my_ball=pygame.image.load("beach_ball.png")
x=random.randint (0,550)  
y=random.randint (0,390)
x_speed=10
y_speed=10
rct=pygame.Rect(0,0,640,480)
rct3=pygame.Rect(160,120,80,80)
rct4=pygame.Rect(400,120,80,80)
rct5=pygame.Rect(160,300,320,80)
def draw_rects():
	pygame.draw.ellipse(screen, [255,255,0], rct)
	pygame.draw.ellipse(screen, [0,0,255], rct3)
	pygame.draw.ellipse(screen, [0,0,255], rct4)
	pygame.draw.ellipse(screen, [255,0,0], rct5)
	pygame.draw.circle(screen, [191,0,191], (x,y), 25)
draw_rects()
pygame.display.flip()
while (True):
    for event in pygame.event.get ():
        if event.type==pygame.QUIT:
            sys.exit ()
    
    pygame.time.delay(20)                                       
    pygame.draw.rect(screen, [255,255,255], [x, y, 90, 90], 0)   
    x = x + x_speed
    y = y + y_speed                             
    if x ==550:     
        x=-90                            
    if y > screen.get_height() - 90  or  y < 0:                
        y_speed = - y_speed
    draw_rects()                                  
    #screen.blit(my_ball, [x, y])                       
    pygame.display.flip() 
      