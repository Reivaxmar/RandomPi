from datetime import datetime

import pygame
import random
import math


pygame.init()

pos = []

# Set up the drawing window
screen = pygame.display.set_mode((400, 400))

random.seed(datetime.now().timestamp())

inside = 0
total = 0
# Run until the user asks to quit
running = True

screen.fill((230, 230, 255))
pygame.draw.circle(screen, (0, 0, 0), (0, 400), 400)
pygame.draw.circle(screen, (0, 0, 255), (0, 400), 398)

while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    pos.append([random.random(), random.random()])
    dist1 = math.sqrt(pos[len(pos)-1][0] ** 2 + (pos[len(pos)-1][1] - 1) ** 2)
    if dist1 <= 1.0:
        pygame.draw.circle(screen, (0, 255, 0), (pos[len(pos)-1][0] * 400.0, pos[len(pos)-1][1] * 400.0), 2)
    else:
        pygame.draw.circle(screen, (255, 0, 0), (pos[len(pos) - 1][0] * 400.0, pos[len(pos) - 1][1] * 400.0), 2)
    for i in range(0, 20000):
        pair = [random.random(), random.random()]
        dist = math.sqrt(pair[0] ** 2 + pair[1] ** 2)
        if dist <= 1.0:
            inside += 1
        total += 1
    print(inside / total * 4)
    print(f"{inside}, {total}")

    pygame.display.flip()

pygame.quit()
