# This is a PyGame example of controlling a ball with mouse, keyboard and joystick.

import pygame
import sys

pygame.init()

joystick_count = pygame.joystick.get_count()
if joystick_count > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    num_axes = joystick.get_numaxes()
    num_buttons = joystick.get_numbuttons()
    print("Found a joystick and initialized it")


WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode([WIDTH, HEIGHT])

fps = 60
timer = pygame.time.Clock()

x = WIDTH // 2
y = HEIGHT // 2
radius = 50
speed = 5
click = False
move_up = False
move_left = False
move_down = False
move_right = False

run = True
while run:
    timer.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
        if event.type == pygame.MOUSEBUTTONUP:
            click = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                move_up = True
            if event.key == pygame.K_a:
                move_left = True
            if event.key == pygame.K_s:
                move_down = True
            if event.key == pygame.K_d:
                move_right = True
            if event.key == pygame.K_ESCAPE:
                run = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                move_up = False
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_s:
                move_down = False
            if event.key == pygame.K_d:
                move_right = False

        # joystick events handle only for specific joystick type (USB - Speedmaster)
        # adapt to your specific joystick type or extend for more joystick types
        if event.type == pygame.JOYAXISMOTION:
            if event.axis == 0:
                if event.value > 0.9:
                    move_right = True
                    move_left = False
                elif event.value < -0.9:
                    move_left = True
                    move_right = False
                else:
                    move_left = False
                    move_right = False
            if event.axis == 1:
                if event.value > 0.9:
                    move_down = True
                    move_up = False
                elif event.value < -0.9:
                    move_up = True
                    move_down = False
                else:
                    move_up = False
                    move_down = False
    if click:
        x, y = pygame.mouse.get_pos()
    if move_up:
        y -= speed
    if move_left:
        x -= speed
    if move_down:
        y += speed
    if move_right:
        x += speed

    screen.fill('black')
    pygame.draw.circle(screen, 'white', (x, y), radius)
    pygame.display.flip()

pygame.quit()
sys.exit()