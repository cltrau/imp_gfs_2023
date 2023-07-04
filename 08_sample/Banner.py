import pygame
from GameConfiguration import GameConfiguration
from ScreenSetup import ScreenSetup
class Banner:
    """Banner class to display the score and lives left"""
    def __init__(self, game_setup: GameConfiguration, screen: ScreenSetup):
        """Initialize the banner"""
        self.game_setup = game_setup
        self.screen = screen
        self.lives = game_setup.count_lives
        self.hit_count = 0
        self.game_over = False

        self.font = pygame.font.SysFont('Calibri', 24, True, False)

    def draw(self):
        """Draw the banner"""
        if self.game_over:
            text_game_over = ""
            if self.game_setup.is_beaten_high_score():
                text_game_over = self.font.render("!! NEW HIGH SCORE - Score: " + str(self.game_setup.get_score()) + " !!", True, 'red')
            else:
                text_game_over = self.font.render("!! GAME OVER - Score: " + str(self.game_setup.get_score()) + " !!", True, 'red')
            x_pos = self.screen.width / 2 - text_game_over.get_size()[0] / 2
            y_pos = self.screen.height - self.screen.banner_height + 2
            self.screen.screen.blit(text_game_over, [x_pos, y_pos])
            return

        color = 'white'
        lives_left = self.lives - self.hit_count
        if lives_left < 0:
            lives_left = 0
        if lives_left == 1:
            color = 'red'
        if lives_left == 2:
            color = 'orange'
        render_text = "Lives: " + str(lives_left) + "/" + str(self.lives)
        y_pos = self.screen.height - self.screen.banner_height + 2
        text = self.font.render(render_text, True, color)
        self.screen.screen.blit(text, [10, y_pos])

        # draw the points on the right side of the banner and pad with zeros
        padded_points = str(self.game_setup.get_points()).zfill(5)
        points_render_text = "Score:" + padded_points
        points_text = self.font.render(points_render_text, True, 'white')
        x_pos = self.screen.width - points_text.get_size()[0] - 10
        self.screen.screen.blit(points_text, [x_pos, y_pos])

    def update_hit_count(self, new_hit_count):
        """Update the hit count"""
        self.hit_count = new_hit_count

    def set_game_over(self):
        """Set the game over flag"""
        self.game_over = True

    def restart_game(self):
        """Restart the game"""
        self.game_over = False
        self.hit_count = 0