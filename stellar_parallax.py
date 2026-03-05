# stellar parallax project
#Zoe, Esther, Torgyn

import pygame
import math
import sys

pygame.init()

screen = pygame.display.set_mode((900, 550))
pygame.display.set_caption("parallax simulator")
clock = pygame.time.Clock()

font = pygame.font.SysFont("arial", 14)
#nme, dist (ly), parallax (arcsec)
stars = [
    ["Proxima Centauri", 4.24, 0.7687],
    ["Alpha Centauri A", 4.37, 0.7421],
    ["Barnards Star", 5.96, 0.5475],
    ["Sirius", 8.60, 0.3792],
    ["Epsilon Eridani", 10.52, 0.3101],
    ["Tau Ceti", 11.91, 0.2739],
    ["Vega", 25.04, 0.1303],
    ["Arcturus", 36.70, 0.0889],
    ["Deneb", 2616.0, 0.00125],
]

current_star = 0

# just testing that it works
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    name = stars[current_star][0]
    label = font.render("star: " + name, True, (255, 255, 255))
    screen.blit(label, (10, 10))

    pygame.display.flip()
    clock.tick(60)