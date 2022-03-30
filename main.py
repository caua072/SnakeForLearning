import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption('Snakegame')

loop = True

snake = [(200, 200), (210,200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))

while loop:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()
