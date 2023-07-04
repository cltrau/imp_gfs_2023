
import pygame

class ScreenSetup:
    """  This class is used to create a screen object.
        Attributes:
            width (int): The width of the screen.
            height (int): The height of the screen.
            fps (int): The frames per second of the screen.
            screen (pygame.Surface): The screen object.
            timer (pygame.time.Clock): The timer object."""
    def __init__(self, width, height, fps):
        self.width = width
        self.height = height
        self.fps = fps
        self.screen = pygame.display.set_mode([self.width, self.height])
        self.timer = pygame.time.Clock()

    def reset_screen(self):
        """This method is used to reset the screen to black."""
        self.screen.fill('black')
        self.timer.tick(self.fps)

    def flip_screen(self):
        """This method is used to flip the screen."""
        pygame.display.flip()