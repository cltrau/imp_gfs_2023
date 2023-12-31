import pygame
from ScreenSetup import ScreenSetup
from Ball import Ball

class GameConfiguration:
    """This class holds the configuration for the game.  It also holds the game state."""


    def __init__(self, lives, new_ball_time, screen: ScreenSetup):
        """Initialize the game configuration.  This includes the number of lives and the time between new balls."""
        self.count_lives = lives
        self.new_ball_time = new_ball_time
        self.screen = screen
        self.player = None
        self.ball_list = []
        self.restart_game()
        self.high_score = 0
        self.score = 0
        self.start_time = pygame.time.get_ticks()
        self.next_ball_time = self.start_time + self.new_ball_time*1000
        self.beaten_high_score = False

    def restart_game(self):
        """Restart the game.  This includes resetting the score and the start time."""
        self.score = 0
        self.start_time = pygame.time.get_ticks()

        self.ball_list.clear()
        self.player = Ball("player", 250, 250, 20, 'green', 1, 1, True, self.screen)
        self.ball_list.append(self.player)
        self.ball_list.append(Ball("blue", 125, 125, 15, 'blue', 1, -0.75, False, self.screen))
        self.ball_list.append(Ball("blue", 375, 125, 15, 'blue', -1, -0.75, False, self.screen))
        self.ball_list.append(Ball("red", 125, 375, 15, 'red', -1, 1.25, False, self.screen))
        self.ball_list.append(Ball("red", 375, 375, 15, 'red', 1.25, -1, False, self.screen))

    def add_ball(self):
        """Add a new ball to the game.  If the new ball collides with an existing ball, don't add it."""
        new_ball = Ball("red", 20, 20, 15, 'red', 1, 1, False, self.screen)
        for ball in self.ball_list:
            if ball.check_collision(new_ball):
                return False
        self.ball_list.append(new_ball)
        return True

    def get_ball_list(self):
        """Return the list of balls in the game."""
        return self.ball_list

    def get_player(self):
        """Return the player ball."""
        return self.player

    def get_points(self):
        """Return the number of points the player has earned."""
        millis_since_start = pygame.time.get_ticks() - self.start_time
        return round(millis_since_start / 1000)

    def get_score(self):
        """Return the score."""
        return self.score

    def is_beaten_high_score(self):
        """Return True if the player has beaten the high score."""
        return self.beaten_high_score

    def check_new_ball(self):
        """Check if it is time to add a new ball."""
        if self.next_ball_time < pygame.time.get_ticks():
            self.next_ball_time = pygame.time.get_ticks() + self.new_ball_time * 1000
            # might not always be able to add a new ball if there is a potential collision in the corner
            self.add_ball()
    def game_over(self):
        """Update the high score if the new score is higher than the current high score."""
        self.score = self.get_points()
        if self.score > self.high_score:
            self.high_score = self.score
            self.beaten_high_score = True
        else:
            self.beaten_high_score = False
