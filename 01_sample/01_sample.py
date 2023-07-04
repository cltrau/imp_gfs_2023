# This is a PyGame skeleton that opens a window and shuts down when the window is closed.
# It is a good starting point for any PyGame project.


import pygame
import sys

pygame.init()

width, height = 400, 400
screen = pygame.display.set_mode((width, height))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
