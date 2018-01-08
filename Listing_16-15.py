# Listing_16-15.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# bounce a beach ball image in a pygame window

import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255, 255, 255])
my_ball = pygame.image.load('beach_ball.png')
x = 50
y = 50
x_speed = 10 
y_speed = 10                           # how fast the ball will move:                                     
                                        # 10 pixels each time through the loop
while (True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    
    pygame.time.delay(20)                                       
    # pygame.draw.rect(screen, [255,255,255], [x, y, 90, 90], 0)   
    x = x + x_speed
    y = y + y_speed                                 # move the ball             
    if x > screen.get_width() - 90  or  x < 0:      # check for hitting the sides            
        x_speed = - x_speed                         # reverse direction            
    if y > screen.get_height() - 90  or  y < 0:      # check for hitting the sides            
        y_speed = - y_speed                         # reverse direction            
    screen.blit(my_ball, [x, y])                       
    pygame.display.flip()                     