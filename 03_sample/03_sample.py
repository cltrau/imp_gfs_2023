# This is a PyGame example of a ball with uniform motion and bouncing off the edges of the screen.

import pygame
import sys


class Ball:
    """This class creates a ball object"""

    def __init__(self, x_pos, y_pos, radius, color, y_speed, x_speed):
        """This method initializes the ball object
                Arguments:
                    x_pos: x position of the ball
                    y_pos: y position of the ball
                    radius: radius of the ball
                    color: color of the ball
                    y_speed: speed of the ball in the y direction
                    x_speed: speed of the ball in the x direction

            """
        self.circle = None
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius
        self.color = color
        self.y_speed = y_speed
        self.x_speed = x_speed

    def draw(self):
        """This method draws the ball object"""
        self.circle = pygame.draw.circle(screen, self.color, (self.x_pos, self.y_pos), self.radius)

    def move(self, width, height):
        """This method moves the ball object.
            If the ball hits the edge of the screen, it bounces back by reversing its direction.
                Arguments:
                    width: width of the screen
                    height: height of the screen
                """
        self.y_pos += self.y_speed
        self.x_pos += self.x_speed
        if self.y_pos < self.radius or self.y_pos > height - self.radius:
            self.y_speed *= -1
        if self.x_pos < self.radius or self.x_pos > width - self.radius:
            self.x_speed *= -1


pygame.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode([WIDTH, HEIGHT])

fps = 60
timer = pygame.time.Clock()

b1 = Ball(50, 50, 30, 'blue', 0, 5)
b2 = Ball(250, 250, 40, 'green', 2, 0)

run = True
while run:
    timer.tick(fps)
    screen.fill('black')

    b1.move(WIDTH, HEIGHT)
    b2.move(WIDTH, HEIGHT)

    b1.draw()
    b2.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()

pygame.quit()
sys.exit()
