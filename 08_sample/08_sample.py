# This is a simple PyGame where the player must avoid hitting other balls.

import random
import sys

import pygame
from ScreenSetup import *
from Ball import Ball
from Banner import Banner
from GameConfiguration import GameConfiguration

# initialize pygame and the joystick
pygame.init()
pygame.joystick.init()

# check if a joystick is connected
joystick_count = pygame.joystick.get_count()
if joystick_count > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    num_axes = joystick.get_numaxes()
    num_buttons = joystick.get_numbuttons()
    print("Joystick detected: " + joystick.get_name())

# create the screen
screen = ScreenSetup(500, 500, 40, 60)

# create the game setup
# 3 lives and new ball every 10 seconds
game_setup = GameConfiguration(3, 10, screen)
hit_count = 0

# create the banner
banner = Banner(game_setup, screen)

flag_increase_red_speed = True
flag_add_ball = False
flag_game_over = False

# main loop
run = True
while run:
    screen.reset_screen()

    # dedicated handling of GAME OVER state
    if flag_game_over:
        start_new_game = False
        banner.draw()
        for ball in game_setup.ball_list:
            ball.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_new_game = True
            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == 3:
                    start_new_game = True

        if start_new_game:
            flag_game_over = False
            hit_count = 0
            game_setup.restart_game()
            banner.restart_game()

    # regular game state
    else:
        for ball in game_setup.get_ball_list():
            ball.reset_bounce_checked()

        for ball in game_setup.get_ball_list():
            for other_ball in game_setup.get_ball_list():
                if ball != other_ball:
                    if not ball.check_bounce_checked():
                        collision = ball.bounce_if_collide(other_ball)
                        if collision:
                            if ball.name == "player" or other_ball.name == "player":
                                if ball.name == "red" or other_ball.name == "red":
                                    hit_count += 1
                                    banner.update_hit_count(hit_count)
                                else:
                                    randBool = random.choice([True, False])
                                    if randBool:
                                        flag_increase_red_speed = True
                                    else:
                                        flag_add_ball = True

        if hit_count >= game_setup.count_lives:
            flag_game_over = True
            banner.set_game_over()
            game_setup.game_over()
            continue

        for ball in game_setup.get_ball_list():
            ball.move()
            ball.draw()

        # update the banner
        banner.draw()

        if flag_increase_red_speed:
            flag_increase_red_speed = False
            for ball in game_setup.get_ball_list():
                if ball.name == "red":
                    ball.change_speed(1)

        if flag_add_ball:
            ball_added = game_setup.add_ball()
            if ball_added:
                flag_add_ball = False

        # add every x seconds a new ball to the game
        game_setup.check_new_ball()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_setup.get_player().flip_full_stop()
                if event.key == pygame.K_RIGHT:
                    game_setup.get_player().change_direction(5)
                if event.key == pygame.K_LEFT:
                    game_setup.get_player().change_direction(-5)
                if event.key == pygame.K_UP:
                    game_setup.get_player().change_speed(1)
                if event.key == pygame.K_DOWN:
                    game_setup.get_player().change_speed(-1)
            elif event.type == pygame.JOYAXISMOTION:
                if event.axis == 0:
                    if event.value > 0.9:
                        game_setup.get_player().change_direction(20)
                    if event.value < -0.9:
                        game_setup.get_player().change_direction(-20)
                if event.axis == 1:
                    if event.value > 0.9:
                        game_setup.get_player().change_speed(-1)
                    if event.value < -0.9:
                        game_setup.get_player().change_speed(1)
            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == 3:
                    game_setup.get_player().flip_full_stop()

    screen.flip_screen()
pygame.quit()
sys.exit()
