import pygame
import sys
import random

#Properties
window_width = 800
window_height = 600
circle_r = 20
circle_x = random.randint(circle_r, window_width-circle_r)
circle_y = random.randint(circle_r, window_height-circle_r)
speed_x = 5
speed_y = 3
multiplier_x = +1
multiplier_y = +1

pygame.init()
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("My First pygamegame Window")

#Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #Keyboard input
        if event.type == pygame.KEYDOWN:
            pass
        #Mouse input
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
    
    window.fill((0, 128, 255))

    #create a circle
    if circle_x >= window_width-circle_r:
        multiplier_x = -1
    elif circle_x < 0+circle_r:
        multiplier_x = +1
    if circle_y >= window_height-circle_r:
        multiplier_y = -1
    elif circle_y < 0+circle_r:
        multiplier_y = +1
    circle_x += speed_x*multiplier_x
    circle_y += speed_y*multiplier_y
    pygame.draw.circle(window, (252, 163, 17), (circle_x, circle_y), circle_r)

    pygame.display.flip()
    pygame.time.Clock().tick(60)  # Limit to 60 FPS
