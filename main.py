from datetime import datetime
import pygame
import random
import math

# Init variables
pygame.init()
screen = pygame.display.set_mode((400, 400))
random.seed(datetime.now().timestamp())
inside = 0
total = 0
running = True

# Clear the screen and draw the circle
screen.fill((230, 230, 255))
pygame.draw.circle(screen, (0, 0, 0), (0, 400), 400)
pygame.draw.circle(screen, (0, 0, 255), (0, 400), 398)

while running:
    # Quit if the application is closed or the Escape key is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Draw the point
    pair1 = [random.random(), random.random()]
    dist1 = math.sqrt(pair1[0] ** 2 + (pair1[1] - 1) ** 2)
    if dist1 <= 1.0:
        pygame.draw.circle(screen, (0, 255, 0), (pair1[0] * 400.0, pair1[1] * 400.0), 2)
    else:
        pygame.draw.circle(screen, (255, 0, 0), (pair1[0] * 400.0, pair1[1] * 400.0), 2)

    # Iterate some more times for a better approximations
    for i in range(0, 20000):
        pair = [random.random(), random.random()]
        dist = math.sqrt(pair[0] ** 2 + pair[1] ** 2)
        if dist <= 1.0:
            inside += 1
        total += 1
    # Print the approximated pi and the inside and total points
    print(inside / total * 4)
    print(f"{inside}, {total}")

    # Display the screen
    pygame.display.flip()

pygame.quit()
