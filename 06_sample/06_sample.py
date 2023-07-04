# This is a PyGame example of balls colliding with each other.

import pygame
import sys
from ScreenSetup import ScreenSetup
from Ball import Ball

pygame.init()
screen = ScreenSetup(500, 500, 60)

# create a list of balls
# Ball(name, x_pos, y_pos, radius, color, x_speed, y_speed, bounce, screen)

ball_list = [Ball("b1-white", 100, 100, 20, 'white', 1, 1, True, screen),
             Ball("b1-blue", 150, 150, 40, 'blue', 1, 1, True, screen),
             Ball("b2-green", 320, 300, 40, 'green', -2, -2, True, screen),
             Ball("b3-red", 400, 400, 23, 'red', 1, 1, True, screen)]

hit_count = 0
run = True
flag_collision_detected = False
while run:
    screen.reset_screen()

    for ball in ball_list:
        ball.reset_bounce_checked()

    for ball in ball_list:
        for other_ball in ball_list:
            # check if the balls are the same
            if ball != other_ball:

                if not ball.check_bounce_checked():
                    hit = ball.bounce_if_collide(other_ball)
                    if hit:
                        hit_count += 1
                        flag_collision_detected = True

    for ball in ball_list:
        ball.move()
        ball.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if flag_collision_detected:
        print("Collisions: " + str(hit_count))
        flag_collision_detected = False

    screen.flip_screen()
pygame.quit()
sys.exit()
