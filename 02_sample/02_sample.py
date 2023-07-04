# This is PyGame example rendering a static circle.

import pygame
import sys

class Ball:
    """This class creates a ball object"""

    def __init__(self, x_pos, y_pos, radius, color):
        """This method initializes the ball object
           Arguments:
              x_pos: x position of the ball
              y_pos: y position of the ball
              radius: radius of the ball
              color: color of the ball"""

        self.circle = None
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius
        self.color = color

    def draw(self):
        """This method draws the ball object"""
        self.circle = pygame.draw.circle(screen, self.color, (self.x_pos, self.y_pos), self.radius)


pygame.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode([WIDTH, HEIGHT])

fps = 60
timer = pygame.time.Clock()

b1 = Ball(250, 250, 30, 'blue')

run = True
black = [0, 0, 0]

while run:

    timer.tick(fps)
    screen.fill('black')
    b1.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()

pygame.quit()
sys.exit()
