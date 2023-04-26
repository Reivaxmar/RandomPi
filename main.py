from datetime import datetime
import pygame
import random
import math
import HardCodes

# Init variables
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode(tuple(map(sum, zip(HardCodes.screenSize, (0, 50)))))
pygame.display.set_caption(HardCodes.title)
random.seed(datetime.now().timestamp())

my_font = pygame.font.SysFont('Comic Sans MS', 32)
inside = 0
total = 0
running = True

# Clear the screen and draw the circle
screen.fill(HardCodes.backColor)
pygame.draw.circle(screen, HardCodes.outlineColor, (0, 400), 400)
pygame.draw.circle(screen, HardCodes.circleColor, (0, 400), 400-HardCodes.outlineSize)

while running:
    # Quit if the application is closed or the Escape key is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 400, 400, 100))
    pygame.draw.rect(screen, HardCodes.backColor, pygame.Rect(HardCodes.outlineSize, 400 + HardCodes.outlineSize, 400 - HardCodes.outlineSize * 2, 50 - HardCodes.outlineSize * 2))


    # Draw the point
    pair1 = [random.random(), random.random()]
    dist1 = math.sqrt(pair1[0] ** 2 + (pair1[1] - 1) ** 2)
    if dist1 <= 1.0:
        pygame.draw.circle(screen, (0, 255, 0), (pair1[0] * 400.0, pair1[1] * 400.0), 2)
    else:
        pygame.draw.circle(screen, (255, 0, 0), (pair1[0] * 400.0, pair1[1] * 400.0), 2)

    # Iterate some more times for a better approximations
    for i in range(0, HardCodes.calcsPerPoint):
        pair = [random.random(), random.random()]
        dist = math.sqrt(pair[0] ** 2 + pair[1] ** 2)
        if dist <= 1.0:
            inside += 1
        total += 1
    # Print the approximated pi and the inside and total points
    if HardCodes.printInConsole:
        print(inside / total * 4)
        print(f"{inside}, {total}")

    text_surface = my_font.render(f"{inside / total * 4}", False, (0, 0, 0))
    screen.blit(text_surface, (10, 401))

    # Display the screen
    pygame.display.flip()

pygame.quit()
