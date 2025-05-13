import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    """
    Represents a shot fired by the player in the game.

    A Shot is a projectile that moves in a straight line and can collide with
    asteroids to destroy or split them. Shots are temporary game objects that
    disappear after a certain distance or upon collision.

    Attributes:
        image (pygame.Surface): The visual representation of the shot.
        rect (pygame.Rect): The rectangular area of the shot for collision detection.
        velocity (pygame.Vector2): The speed and direction of the shot's movement.
        lifespan (float): The time (in seconds) the shot remains active before disappearing.
    """

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: pygame.surface) -> pygame.Rect:
        pygame.draw.circle(screen, "white", (self.position), self.radius, 2)

    def update(self, dt: float) -> pygame.Vector2:
        self.position += self.velocity * dt
