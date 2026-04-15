import pygame
import random
pygame.init()

#Screen
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

#Colors
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
black = (0,0,0)

#Snake
snake_block = 10
snake_speed = 20

clock = pygame.time.Clock()

def game():
    x=width//2
    y = height//2

    dx =0
    dy =0

    snake = []
    length = 1

    food_x = random.randrange(0,width,snake_block)
    food_y = random.randrange(0,height,snake_block)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -snake_block
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = snake_block
                    dy = 0

                elif event.key == pygame.K_UP:
                    dy=-snake_block
                    dx=0
                elif event.key == pygame.K_DOWN:
                    dy = snake_block
                    dx = 0

        x += dx
        y += dy

        screen.fill(black)

        pygame.draw.rect(screen, red, [food_x, food_y,snake_block,snake_block])

        snake.append([x,y])
        if len(snake)> length:
            del snake[0]

        for block in snake:
            pygame.draw.rect(screen, green, [block[0], block[1],snake_block,snake_block])

        if x == food_x and y == food_y:
            food_x = random.randrange(0,width,snake_block)
            food_y = random.randrange(0,height,snake_block)
            length += 1

        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
game()