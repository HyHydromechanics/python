import pygame
from pygame.locals import QUIT, KEYDOWN, K_f, FULLSCREEN
from sys import exit
 
background_image_filename = "./images/sushiplate.jpg"
 
pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
size = width, height= 640, 480
color = (0,0,0)

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
speed = [5,5]
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            exit() 

    ballrect = ballrect.move(speed)
    if ballrect.left<0 or ballrect.right>width:
        speed[0]=-speed[0]
    if ballrect.top<0 or ballrect.bottom>height:
        speed[1] = -speed[1]
        
    screen.fill(color)
    screen.blit(ball, ballrect)
    pygame.display.flip()
