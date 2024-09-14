import pygame
import random
from pygame.locals import *

pygame.init()

w = 800
h = 600
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("aim trainer")

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

target_radius = 30
target_pos1 = (random.randint(30,770), random.randint(30,570))
target_pos2 = (random.randint(30,770), random.randint(30,570))
target_pos3 = (random.randint(30,770), random.randint(30,570))

score = 0
misses = 0

flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()
            distance1 = pygame.math.Vector2(target_pos1).distance_to(click_pos)
            distance2 = pygame.math.Vector2(target_pos2).distance_to(click_pos)
            distance3 = pygame.math.Vector2(target_pos3).distance_to(click_pos)
            if distance1 < target_radius:
                score += 1
                target_pos1 = (random.randint(target_radius, w - target_radius),
                              random.randint(target_radius, h - target_radius))
                pygame.draw.circle(screen, red, target_pos1, target_radius)
            elif distance2 < target_radius:
                score += 1
                target_pos2 = (random.randint(target_radius, w - target_radius),
                               random.randint(target_radius, h - target_radius))
                pygame.draw.circle(screen, red, target_pos2, target_radius)
            elif distance3 < target_radius:
                score += 1
                target_pos3 = (random.randint(target_radius, w - target_radius),
                               random.randint(target_radius, h - target_radius))
                pygame.draw.circle(screen, red, target_pos3, target_radius)
            else:
                misses+=1
                if misses>=3:
                    print("Score: "+str(score))
                    flag=False
        if event.type == pygame.QUIT:
            flag = False
            pygame.quit()
            exit()

    screen.fill(black)
    pygame.draw.circle(screen, red, target_pos1, target_radius)
    pygame.draw.circle(screen, red, target_pos2, target_radius)
    pygame.draw.circle(screen, red, target_pos3, target_radius)

    pygame.display.update()




