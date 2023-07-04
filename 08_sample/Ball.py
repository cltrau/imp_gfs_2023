from ScreenSetup import ScreenSetup
import pygame


class Ball:
    """This class is used to create a ball object."""

    SPEED_CHANGE_FACTOR = 0.1

    def __init__(self, name, x_pos, y_pos, radius, color, x_direction, y_direction, draw_direction_indicator, screen: ScreenSetup):
        """This method is used to initialize a ball object.
           Attributes:
                name (str): The name of the ball object.
                x_pos (int): The x position of the ball object.
                y_pos (int): The y position of the ball object.
                radius (int): The radius of the ball object.
                color (str): The color of the ball object.
                x_direction (int): The x direction of the ball object.
                y_direction (int): The y direction of the ball object.
                draw_direction_indicator (bool): The draw direction indicator attribute of the ball object.
                screen (ScreenSetup): The screen object.
        """
        self.name = name
        self.pos = pygame.math.Vector2(x_pos, y_pos)
        self.dir = pygame.math.Vector2(x_direction, y_direction)
        self.radius = radius
        self.color = color
        self.bounce_checked = False
        self.draw_direction_indicator = draw_direction_indicator
        self.screen_definition = screen

        self.before_stop_dir = pygame.math.Vector2(self.dir)
        self.full_stop_flag = False
        self.increase_radius_flag = False

    def reset_bounce_checked(self):
        """This method is used to reset the bounce checked attribute of the ball object."""
        self.bounce_checked = False

    def check_bounce_checked(self):
        """This method is used to check the bounce checked attribute of the ball object."""
        return self.bounce_checked

    def draw(self):
        """This method is used to draw the ball object on the screen."""
        self.circle = pygame.draw.circle(self.screen_definition.screen, self.color, self.pos,
                                         self.radius)
        if self.draw_direction_indicator:
            norm_dir = pygame.math.Vector2(self.dir)
            norm_dir.scale_to_length(self.radius-2)
            rad_dir = self.pos + norm_dir
            pygame.draw.line(self.screen_definition.screen, 'black', self.pos, rad_dir, 2)

    def change_direction(self, angel):
        """This method is used to change the direction of the ball object.
           Attributes:
                angel (int): The angel of the direction change.
        """
        if self.full_stop_flag:
            self.before_stop_dir.rotate_ip(angel)
        self.dir.rotate_ip(angel)

    def move(self):
        """This method is used to move the ball object."""
        self.pos += self.dir
        if self.pos.y < self.radius or self.pos.y > self.screen_definition.get_playground_height() - self.radius:
            self.dir.y *= -1
        if self.pos.x < self.radius or self.pos.x > self.screen_definition.get_playground_width() - self.radius:
            self.dir.x *= -1

    def next_move_position(self):
        """This method is used to calculate the next move position of the ball object."""
        return self.pos + self.dir

    def position_vector(self):
        """This method is used to return the position vector of the ball object."""
        return self.pos

    def direction_vector(self):
        """This method is used to return the direction vector of the ball object."""
        return self.dir

    def update_direction(self, direction_vector: pygame.math.Vector2):
        """This method is used to update the direction vector of the ball object.
           Attributes:
                direction_vector (pygame.math.Vector2): The direction vector of the ball object.""
        """

        self.dir.x = direction_vector.x
        self.dir.y = direction_vector.y

    def bounce(self, bounce_surface: pygame.math.Vector2):
        """This method is used to bounce the ball object.
              Attributes:
                     bounce_surface (pygame.math.Vector2): The bounce surface of the ball object.
        """
        bounced_vector = self.direction_vector().reflect(bounce_surface)
        self.dir.x = bounced_vector.x * -1
        self.dir.y = bounced_vector.y * -1

    def collide_direction(self, other_ball):
        """This method is used to calculate the direction vector of the ball object after a collision.
              Attributes:
                        other_ball (Ball): The other ball object.
        """

        pp = self.pos - other_ball.pos
        pp.rotate(90)
        return self.dir.reflect(pp)


    def check_collision(self, other_ball):
        """This method is used to check if the ball object would collide with another ball object.
              Attributes:
                        other_ball (Ball): The other ball object.
        """
        v1 = self.position_vector()
        v2 = other_ball.position_vector()

        if v1.distance_to(v2) < self.radius + other_ball.radius:
            return True
        else:
            return False
    def bounce_if_collide(self, other_ball):
        """This method is used to bounce the ball object if it collides with another ball object.
                Attributes:
                        other_ball (Ball): The other ball object.
        """
        v1 = self.position_vector()
        v2 = other_ball.position_vector()

        if v1.distance_to(v2) < self.radius + other_ball.radius:
            d1 = self.collide_direction(other_ball)
            d2 = other_ball.collide_direction(self)
            self.update_direction(d1)
            other_ball.update_direction(d2)
            self.bounce_checked = True
            other_ball.bounce_checked = True
            return True
        else:
            return False

    def flip_full_stop(self):
        if self.full_stop_flag:
            self.full_stop_flag = False
            self.continue_moving()
        else:
            self.full_stop_flag = True
            self.full_stop()

    def full_stop(self):
        """This method is used to stop the ball object."""
        self.before_stop_dir.x = self.dir.x
        self.before_stop_dir.y = self.dir.y

        # set direction to nearly zero to stop the ball
        self.dir.x = self.dir.x * 0.00001
        self.dir.y = self.dir.y * 0.00001

    def continue_moving(self):
        """This method is used to continue moving the ball object."""
        self.dir.x = self.before_stop_dir.x
        self.dir.y = self.before_stop_dir.y

    def change_speed(self, direction):
        """This method is used to change the speed of the ball object.
                    Attributes:
                            direction (int): 1 for increase, -1 for decrease.
            """
        if self.full_stop_flag:
            # no speed change if ball is stopped
            return
        dir_length = self.dir.length()

        if direction > 0:
            dir_length += dir_length * Ball.SPEED_CHANGE_FACTOR
        else:
            dir_length -= dir_length * Ball.SPEED_CHANGE_FACTOR

        # don't change speed if upper or lower bound is reached
        if dir_length > 5 or dir_length < 0.25:
            return
        self.dir.scale_to_length(dir_length)
