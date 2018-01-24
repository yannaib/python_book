import pygame, sys, random
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255, 255, 255])
my_ball = pygame.image.load('beach_ball.png')
x = random.randint (0,550)
y = random.randint (0,390)
x_speed = 5
#y_speed = 10         
while (True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    
    pygame.time.delay(20)                                       
    pygame.draw.rect(screen, [255,255,255], [x, y, 90, 90], 0)   
    x = x + x_speed
    #y = y + y_speed                             
    if x ==550:     
        x=-90                            
    #if y > screen.get_height() - 90  or  y < 0:                
        #y_speed = - y_speed                                  
    screen.blit(my_ball, [x, y])                       
    pygame.display.flip()                    
