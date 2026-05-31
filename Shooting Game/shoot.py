import pygame
import random

pygame.init()

#Screen
WIDTH, HEIGHT = 600,1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooting Game")

#colors
WHITE = (255,255,255)
RED = (255,0,0)

#Player
player = pygame.Rect(280,800,40,40)

#Enemy
enemy = pygame.Rect((random.randint(0,560)),0,40,40)

#Bullet
bullet = pygame.Rect(0,0,5,10)
bullet_active = False

#Speed
player_speed = 5
enemy_speed = 1
bullet_speed = 5

#Score
score = 0
font = pygame.font.SysFont(None,30)

#Game Loop
running = True
while running:
    screen.fill((0,0,0))

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Keys
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < WIDTH - 40:
        player.x += player_speed

    #Shoot bullet
    if keys[pygame.K_SPACE] and not bullet_active:
        bullet.x = player.x + 18
        bullet.y = player.y
        bullet_active = True

    #move Bullet
    if bullet_active:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullet_active = False

    #Move enemy
    enemy.y += enemy_speed
    if enemy.y > HEIGHT:
        enemy.x = random.randint(0,560)
        enemy.y = 0

    # Collision
    if bullet.colliderect(enemy):
        score += 1
        bullet_active = False
        enemy.x = random.randint(0, 560)
        enemy.y = 0

    #draw Object
    pygame.draw.rect(screen,WHITE,player)
    pygame.draw.rect(screen,RED,enemy)
    if bullet_active:
        pygame.draw.rect(screen,WHITE,bullet)

    #Show Score
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10,10))

    pygame.display.update()

pygame.quit()