import pygame
from pygame.locals import *

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

my_dir = RIGHT

pygame.init()

screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption('Snakegame')

loop = True

clock = pygame.time.Clock()

snake = [(200, 200), (210,200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))

while loop:

    clock.tick(20)

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            
            if event.key == pygame.K_w:
                my_dir = UP
            if event.key == pygame.K_d:
                my_dir = RIGHT
            if event.key == pygame.K_s:
                my_dir = DOWN
            if event.key == pygame.K_a:
                my_dir = LEFT

    for pos in snake:
        screen.blit(snake_skin, pos)

    if my_dir == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])

    if my_dir == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_dir == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
    if my_dir == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)

    pygame.display.update()
