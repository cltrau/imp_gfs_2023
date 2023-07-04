# This is a PyGame example of a ball under gravity and acceleration.

import pygame
import sys


class GravityDefinition:
    """This class defines the gravity for a ball object"""

    def __init__(self, height, acceleration, final_stop_speed):
        """This method initializes the gravity definition
                Arguments:
                    height: height of the screen
                    acceleration: acceleration of the ball
                    final_stop_speed: final stop speed of the ball
                """
        self.height = height
        self.acceleration = acceleration
        self.final_stop_speed = final_stop_speed


class Ball:
    """This class creates a ball object"""

    def __init__(self, x_pos, y_pos, radius, color, y_speed, absorption, gravity_configuration: GravityDefinition):
        """This method initializes the ball object
                Arguments:
                    x_pos: x position of the ball
                    y_pos: y position of the ball
                    radius: radius of the ball
                    color: color of the ball
                    y_speed: speed of the ball in the y direction
                    absorption: absorption of the ball
                    gravity_configuration: gravity definition of the ball
                """
        self.circle = None
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius
        self.color = color
        self.y_speed = y_speed
        self.x_speed = 0
        self.absorption = absorption
        self.gravity_configuration = gravity_configuration

    def draw(self):
        """This method draws the ball object"""
        self.circle = pygame.draw.circle(screen, self.color, (self.x_pos, self.y_pos), self.radius)

    def gravity(self):
        """This method calculates the gravity for the ball object and applies it to the ball speed in the y direction"""

        # as long as the ball is not at the bottom of the screen, the ball is accelerated
        if self.y_pos < self.gravity_configuration.height - self.radius:
            self.y_speed += self.gravity_configuration.acceleration
        else:
            # if the ball hits the bottom of the screen, it bounces back
            if self.y_speed > self.gravity_configuration.final_stop_speed:
                self.y_speed = self.y_speed * -1 * self.absorption
            else:
                # if the ball is almost at rest, it stops
                if abs(self.y_speed) <= self.gravity_configuration.final_stop_speed:
                    self.y_speed = 0
        return self.y_speed

    def move(self):
        """This method moves the ball object"""
        self.y_pos += self.y_speed
        self.x_pos += self.x_speed


pygame.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode([WIDTH, HEIGHT])

fps = 60
timer = pygame.time.Clock()

# define the gravity
# height of the screen, acceleration of the ball, final stop speed of the ball
gravity_definition = GravityDefinition(HEIGHT, 0.1, 0.2)

# adjust absorption to see the effect
# absorption factor of 0.75 means that the ball will bounce back with 75% of the speed it hit the ground
b1_absorption = 0.75
b2_absorption = 0.9

b1 = Ball(50, 50, 30, 'blue', 0, b1_absorption, gravity_definition)
b2 = Ball(250, 50, 40, 'green', 0, b2_absorption, gravity_definition)

run = True
while run:
    timer.tick(fps)
    screen.fill('black')

    b1.draw()
    b2.draw()
    b1.move()
    b2.move()

    b1.gravity()
    b2.gravity()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()
sys.exit()
