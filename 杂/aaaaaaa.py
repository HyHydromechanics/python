import pygame

pygame.init()
size = width, height = 1080, 720
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Example")


class Button:
    def _init_(self, screen_example, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width = 200
        self.height = 50
        self.button_color = (0, 255, 0)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.prep_msg(msg)
