import pygame, random, time
from pygame.locals import *

def collisions(obj1, obj2):
    
    return((obj1[0] == obj2[0]) and (obj1[1] == obj2[1]))

def Text(font_dir, size, text, color, x, y):

    font = pygame.font.Font(font_dir, size)

    font_render = font.render(text, True, color)
    font_rect = font_render.get_rect()
    font_rect = (x, y)
    screen.blit(font_render, font_rect)

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

color = (255, 255, 255)

my_dir = LEFT

pygame.init()

screen = pygame.display.set_mode([400, 400])
pygame.display.set_caption('Snakegame')

loop = True

clock = pygame.time.Clock()

snake = [(200, 200), (210,200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill(color)

apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))

#apple_pos = ((random.randint(0, 500)//10 * 10, random.randint(0, 500)//10 * 10))
#apple_pos = ((random.randrange(0, 500, 10), random.randrange(0, 500, 10)))
apple_pos = ((random.randint(0, 40) * 10, random.randint(0,40) * 10))
print(apple_pos)

pts = 0

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

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    if collisions(snake[0], apple_pos):
        snake.append((-10,-10))
        apple_pos = ((random.randint(0, 40) * 10, random.randint(0,40) * 10))
        pts += 1
        print(pts)
        print(apple_pos)
    

    if my_dir == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])

    if my_dir == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_dir == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
    if my_dir == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)


    for x in range(1, len(snake)):
        if snake[0][0] == snake[x][0] and snake[0][1] == snake[x][1]:
            pygame.time.wait(1000)
            pygame.quit()
            exit()
    
    
    
    if snake[0][0] >= 400 or snake[0][0] <= 0:
        pygame.time.delay(1000)
        pygame.quit()
        exit()
    elif snake[0][1] >= 400 or snake[0][1] <= 0:
        pygame.time.delay(1000)
        pygame.quit()
        exit()
        
    for x in range(0, 400, 10):
        pygame.draw.line(screen, (40, 40, 40), (x,0), (x, 400))
    for y in range(0, 400, 10):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (400, y))

    screen.blit(apple, apple_pos)

    score = Text('font/font.ttf', 24, 'Score: %s' % (pts), (54, 186, 158), 10, 10)

    pygame.display.update()
