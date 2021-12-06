import pygame
import sys
from pygame.locals import *

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

size = width, height = 1080, 720
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Harry")
position = size[0] // 2, size[1] // 2
moving = False
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                moving = True

        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                moving = False

    if moving:
        position = pygame.mouse.get_pos()

    screen.fill(white)

    pygame.draw.circle(screen, black, position, 50, 1)
    pygame.draw.circle(screen, red, position, 100, 1)
    pygame.draw.circle(screen, blue, position, 150, 1)

    pygame.display.flip()

    clock.tick(120)
