import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption('Snakegame')

loop = True

while loop:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    pygame.display.update()