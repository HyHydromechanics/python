from moviepy.editor import *
import pygame

pygame.display.set_caption('Hello World!')

clip = VideoFileClip('1.flv')
clip.preview()

pygame.quit()
