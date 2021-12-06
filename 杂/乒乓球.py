import pygame
import sys
from pygame.locals import *
clock = pygame.time.Clock()
pygame.init()

size = width, height = 1080,720
speed = [0,0]
bg = (255,255,255)
fullscreen = False
moving = False

screen = pygame.display.set_mode(size, RESIZABLE)
pygame. display.set_caption("PING PANG BALL")
ball = pygame. image. load("ball.png").convert_alpha()
position = ball.get_rect()
pat_1 = pygame.image.load()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_k:
                sys.exit()
            if event.key == K_a:
                speed = [-5,0]
                ball = pygame.transform.flip(ball, True, True)
            if event.key == K_w:
                speed = [0,-5]
                ball = pygame.transform.flip(ball, True, True)
            if event.key == K_s:
                speed = [0,5]
                ball = pygame.transform.flip(ball, True, True)
            if event.key == K_d:
                speed = [5,0]
                ball = pygame.transform.flip(ball, True, True)
            if event.key == K_LEFT:
                speed = [-5,0]
                ball = pygame.transform.flip(ball, True, True)
            if event.key == K_UP:
                speed = [0,-5]
                ball = pygame.transform.flip(ball, True, True)
            if event.key == K_DOWN:
                speed = [0,5]
                ball = pygame.transform.flip(ball, True, True)
            if event.key == K_RIGHT:
                speed = [5,0]
                ball = pygame.transform.flip(ball, True, True)
                
            if event.key == K_F1:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((1920, 1080),FULLSCREEN | HWSURFACE)
                else:
                    if event.key == K_F2:
                        screen = pygame.display.set_mode(size)

        if event.type == VIDEORESIZE:
                size = event.size
                width, height = size
                screen = pygame.display.set_mode(size, RESIZABLE)
                
    position = position.move(speed)

    if position.left < 0 or position.right > width:
        ball = pygame.transform.flip(ball, True, True)
        speed[0]= -speed[0]
    
    if position.top<0 or position.bottom > height:
        ball = pygame.transform.flip(ball, True, True)
        speed[1] = -speed[1]

    screen.fill(bg)
    screen.blit(ball, position)
    pygame.display.flip()
    clock.tick(200)
