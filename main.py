# Simple pygame program

# Import and initialize the pygame library
import pygame
import random
import math

pygame.init()

pos = []

# Set up the drawing window
screen = pygame.display.set_mode((400, 400))

inside = 0
total = 0
# Run until the user asks to quit
running = True

screen.fill((255, 255, 255))
pygame.draw.circle(screen, (0, 0, 255), (0, 400), 400)

while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    pos.append([random.randrange(0, 399), random.randrange(0, 399)])
    pygame.draw.circle(screen, (0, 0, 0), (pos[len(pos)-1][0] - 1, pos[len(pos)-1][1] - 1), 2)
    for i in range(0, 20000):
        pair = [random.randrange(0, 399), random.randrange(0, 399)]
        dist = math.dist(pair, [0, 250])
        if dist <= 400.0:
            inside += 1
        total += 1
    print(inside / total * 4)
    print(f"{inside}, {total}")

    pygame.display.flip()

pygame.quit()
