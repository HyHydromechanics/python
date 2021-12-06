#一共有三个物品, ball, pat_1, pat_2
#拍子击中加一分? or 拍子漏掉对面加分?
#pat_1和2是动的, 球只会反弹
#拍子都在两侧中间, 球在中心
import pygame
import sys
import random
from pygame import *
clock = pygame.time.Clock()
pygame.init()

#设置窗口
size = width, height = 1080,720
speed_1 = [0,0]
speed_2 = [0,0]
speed_3 = [680,720]
bg = (0,0,0)

#设置背景与标题
screen = pygame.display.set_mode(size) 
pygame. display.set_caption("Pingpang Ball")

#导入球图片
ball = pygame. image. load("ball.png").convert_alpha()
ball_position = ball.get_rect()

#导入拍子
pat_1 = pygame.image.load("pat_1.png").convert_alpha()
pat_1_position = pat_1.get_rect()
pat_2 = pygame.image.load("pat_2.png").convert_alpha()
pat_2_position = pat_2.get_rect()

#关闭窗口
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            #写入keydown, pat_1的
        if event.type == KEYDOWN:
            if event.key == K_a:
                speed_1 = [-5,0]
                pat_1 = pygame.transform(pat_1, True, True)
            if event.key == K_w:
                speed_1 = [0,-5]
                pat_1 = pygame.transform(pat_1, True, True)
            if event.key == K_s:
                speed_1 = [0,5]
                pat_1 = pygame.transform(pat_1, True, True)
            if event.key == K_d:
                speed_1 = [5,0]
                pat_1 = pygame.transform(pat_1, True, True)
            #写入keydown, pat_2的
            #bug: module' object is not callable
            if event.key == K_LEFT:
                speed_2 = [-5,0]
                pat_2 = pygame.transform(pat_2, False, False)
            if event.key == K_UP:
                speed_2 = [0,-5]
                pat_2 = pygame.transform(pat_2, True, True)
            if event.key == K_DOWN:
                speed_2 = [0,5]
                pat_2 = pygame.transform(pat_2, True, True)
            if event.key == K_RIGHT:
                speed_2 = [5,0]
                pat_2 = pygame.transform(pat_2, True, True)

                
            #反向来一遍_keyup的
        if event.type == KEYUP:
            if event.key == K_a:
                speed_1 = [0,0]
                pat_1 = pygame.transform(pat_1, True, True)
            if event.key == K_w:
                speed_1 = [0,0]
                pat_1 = pygame.transform(pat_1, True, True)
            if event.key == K_s:
                speed_1 = [0,0]
                pat_1 = pygame.transform(pat_1, True, True)
            if event.key == K_d:
                speed_1 = [0,0]
                pat_1 = pygame.transform(pat_1, True, True)
            #写入keyup, pat_2的
            if event.key == K_LEFT:
                speed_2 = [0,0]
                pat_2 = pygame.transform(pat_2, True, True)
            if event.key == K_UP:
                speed_2 = [0,0]
                pat_2 = pygame.transform(pat_2, True, True)
            if event.key == K_DOWN:
                speed_2 = [0,0]
                pat_2 = pygame.transform(pat_2, True, True)
            if event.key == K_RIGHT:
                speed_2 = [0,0]
                pat_2 = pygame.transform(pat_2, True, True)

    pat_1_position = pat_1_position.move(speed_1)
    pat_2_position = pat_2_position.move(speed_2)

#设定 拍子触碰变方向, pat_1
    if pat_1_position.left < 0 or pat_1_position.right > width:
        speed_3[0]= -speed_3[0]
    
    if pat_2_position.top<0 or pat_2_position.bottom > height:
        speed_3[1] = -speed_3[1]

#此行有bug
#AttributeError: 'list' object has no attribute 'left'
    if ball_position.left < 0 or ball_position.right > width:
        ball = pygame.transform.flip(ball, True, True)
        speed_3[0]= -speed_3[0]
    
    if ball_position.top<0 or ball_position.bottom > height:
        ball = pygame.transform.flip(ball, True, True)
        speed_3[1] = -speed_3[1]

    screen.fill(bg)
#刷新屏幕
    screen.blit(ball, speed_3)
    screen.blit(pat_1, speed_2)
    screen.blit(pat_2, speed_1)
    pygame.display.flip()
    clock.tick(200)
