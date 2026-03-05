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
earth_ang=0
paused = False

# siwtch through the stars
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_SPACE:
                paused = not paused
            if event.key == pygame.K_RIGHT:
                current_star = current_star + 1
                if current_star >= len(stars):
                    current_star = 0
            if event.key == pygame.K_LEFT:
                current_star = current_star - 1
                if current_star < 0:
                    current_star = len(stars) - 1
    if not paused:
        earth_ang = earth_ang + 0.02
        if earth_ang >= 2 * math.pi:
            earth_ang = earth_ang - 2 * math.pi
    
    screen.fill((0, 0, 0))
    sun_x = 200
    sun_y = 260

    name = stars[current_star][0]
    parallax = stars[current_star][2]

    #orbit
    pygame.draw.circle(screen,(60,60,60),(sun_x, sun_y), 110, 1)
    pygame.draw.circle(screen,(255, 220,0),(sun_x,sun_y),15)
    label = font.render("sun",True,(255,220,0))

    screen.blit(label,(sun_x-10, sun_y+20))
    earth_x = int(sun_x + 110 * math.cos(earth_ang))
    earth_y = int(sun_y + 110 * math.sin(earth_ang))
    pygame.draw.circle(screen,(0, 100, 255),(earth_x, earth_y), 10)
    label_2 = font.render("earth", True, (100, 150, 255))

    screen.blit(label_2, (earth_x +10, earth_y -5))
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    mindex = int(earth_ang / (2 * math.pi) * 12)%12
    month_label = font.render(months[mindex], True, (100, 150, 255))
    screen.blit(month_label, (earth_x - 10, earth_y -20))

    #other view
    pygame.draw.circle(screen, (255,50,50),(410,sun_y),5)
    label_3 = font.render(stars[current_star][0], True, (255, 50, 50))
    screen.blit(label_3, (410, sun_y - 10))

    #line earth to star
    pygame.draw.line(screen,(100,100,100),(earth_x,earth_y),(410,sun_y),1)
    
    #divider
    pygame.draw.line(screen,(50,50,50),(450,0),(450,550),1)
    screen.blit(font.render("solar system view",True,(100,100,100)),(10,10))

    screen.blit(font.render("sky view",True,(100,100,100)),(460,10))

    sky_cx = 680
    sky_cy = 250

    #how much star shifts (proxima is max shift)
    shift = (parallax / 0.7687) * 120*math.cos(earth_ang)
    star_x = int(sky_cx + shift)
    
    #target 
    pygame.draw.circle(screen,(255,50,50),(star_x,sky_cy),5)
    screen.blit(font.render(name,True,(255,50,50)),(star_x-20, sky_cy-20))

    #center line
    pygame.draw.line(screen,(50,50,50),(sky_cx,100),(sky_cx,420),1)
    pygame.draw.line(screen,(255,200,0),(sky_cx,sky_cy+35),(star_x,sky_cy+35),2)
    shift_label = f"shift = {abs(shift):.1f} px"
    screen.blit(font.render(shift_label, True, (255,200,0)),
                (int((sky_cx + star_x) / 2) - 30, sky_cy + 40))
    
    name = stars[current_star][0]
    label = font.render("star: " + name, True, (255, 255, 255))
    screen.blit(label, (10, 10))

    pygame.display.flip()
    clock.tick(60)