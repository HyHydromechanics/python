import pygame
import sys
from pygame.locals import *

clock = pygame.time.Clock()
pygame.init()

# 设置屏幕
size = width, height = [1080, 720]
pat = (
    "pat_1.png"
    "pat_2.png"
)
speed_pat_1 = [0, 0]
speed_pat_2 = [900, 0]
speed_ball = [540, 360]
bg = (100, 255, 100)
fullscreen = False
moving = False

# 导入图片
screen = pygame.display.set_mode(size, RESIZABLE)
pygame.display.set_caption("Moving Ball")
ball = pygame.image.load("ball.png").convert_alpha()
pat_1 = pygame.image.load("pat_1.png").convert_alpha()
pat_2 = pygame.image.load("pat_2.png").convert_alpha()
position_pat = pat.get.rect()
position_pat_1 = pat_1.get_rect()
position_pat_2 = pat_2.get_rect()
position_ball = ball.get_rect()

# 写入系统(修改屏幕, 退出等)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == VIDEORESIZE:
            size = event.size
            width, height = size
            screen = pygame.display.set_mode(size, RESIZABLE)
# 写入player_1 运动模式
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_a:
                speed_pat_1 = [-5, 0]
                pat_1 = pygame.transform.flip(pat_1, False, False)
            if event.key == K_w:
                speed_pat_1 = [0, -5]
                ball = pygame.transform.flip(pat_1, False, False)
            if event.key == K_s:
                speed_pat_1 = [0, 5]
                pat_1 = pygame.transform.flip(pat_1, False, False)
            if event.key == K_d:
                speed_pat_1 = [5, 0]
                pat_1 = pygame.transform.flip(pat_1, False, False)
# 写入player_2 运动模式
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                speed_pat_2 = [-5, 0]
                pat_2 = pygame.transform.flip(pat_2, False, False)
            if event.key == K_UP:
                speed_pat_2 = [0, -5]
                pat_2 = pygame.transform.flip(pat_2, False, False)
            if event.key == K_DOWN:
                speed_pat_2 = [0, 5]
                pat_2 = pygame.transform.flip(pat_2, False, False)
            if event.key == K_RIGHT:
                speed_pat_2 = [5, 0]
                pat_2 = pygame.transform.flip(pat_2, False, False)

        if event.type == KEYUP:
            if event.key == K_a:
                speed_pat_1 = [0, 0]
                pat_1 = pygame.transform(pat_1, False, False)
            if event.key == K_w:
                speed_pat_1 = [0, 0]
                pat_1 = pygame.transform(pat_1, False, False)
            if event.key == K_s:
                speed_pat_1 = [0, 0]
                pat_1 = pygame.transform(pat_1, False, False)
            if event.key == K_d:
                speed_pat_1 = [0, 0]
                pat_1 = pygame.transform(pat_1, False, False)
            # 写入key up, pat_2的
            if event.key == K_LEFT:
                speed_pat_2 = [0, 0]
                pat_2 = pygame.transform(pat_2, False, False)
            if event.key == K_UP:
                speed_pat_2 = [0, 0]
                pat_2 = pygame.transform(pat_2, False, False)
            if event.key == K_DOWN:
                speed_pat_2 = [0, 0]
                pat_2 = pygame.transform(pat_2, False, False)
            if event.key == K_RIGHT:
                speed_pat_2 = [0, 0]
                pat_2 = pygame.transform(pat_2, False, False)

# 写入position
    position_ball = position_ball.move(speed_ball)
    position_pat_1 = position_pat_1.move(speed_pat_1)
    position_pat_2 = position_pat_2.move(speed_pat_2)

# 写入球的运动轨迹(待补充, 碰撞)
    if position_ball.left < 0 or position_ball.right > width:
        ball = pygame.transform.flip(ball, True, True)
        speed_ball[0] = -speed_ball[0]
    if position_ball.top < 0 or position_ball.bottom > height:
        ball = pygame.transform.flip(ball, True, True)
        speed_ball[1] = -speed_ball[1]

    if position_pat_1.left < 0 or position_pat_1 > width:
        pat_1 = pygame.transform.flip(pat_2, False, False)
        speed_pat_1 = [0, 0]
    if position_pat_1.top < 0 or position_pat_1.bottom > height:
        ball = pygame.transform.flip(ball, False, False)
        speed_pat_1 = [0, 0]

    if position_pat_2.left < 0 or position_pat_2 > width:
        pat_1 = pygame.transform.flip(pat_2, False, False)
        speed_pat_2 = [0, 0]
    if position_pat_2.top < 0 or position_pat_2.bottom > height:
        ball = pygame.transform.flip(ball, False, False)
        speed_pat_2 = [0, 0]
# you know
    screen.fill(bg)
    screen.blit(ball, position_ball)
    screen.blit(pat_1, position_pat_1)
    screen.blit(pat_2, position_pat_2)
    pygame.display.flip()
    clock.tick(200)
