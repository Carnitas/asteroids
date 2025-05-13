import random

import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    """
    Represents an asteroid in the game.

    An Asteroid is a game object that moves across the screen and can collide
    with the player or shots. Upon collision with a shot, it splits into smaller
    asteroids or is destroyed. Asteroids are part of the game's dynamic elements
    and are managed within the asteroid field.

    Attributes:
        image (pygame.Surface): The visual representation of the asteroid.
        rect (pygame.Rect): The rectangular area of the asteroid for collision detection.
        velocity (tuple[float, float]): The speed and direction of the asteroid's movement.
        size (int): The size of the asteroid, determines its scale and behavior upon splitting.
    """

    def draw(self, screen: pygame.surface) -> pygame.Rect:
        pygame.draw.circle(screen, "white", (self.position), self.radius, 2)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        new_velocity_1 = self.velocity.rotate(random_angle)
        new_velocity_2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_velocity_1 * 1.2
        asteroid2.velocity = new_velocity_2 * 1.2
