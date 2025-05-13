import pygame


class CircleShape(pygame.sprite.Sprite):
    """
    A base class representing a circular shape in the game.

    CircleShape provides common functionality for circular game objects, such as
    position, radius, and basic movement. It serves as a parent class for specific
    game elements like asteroids and shots.

    Attributes:
        position (pygame.Vector2): The position of the circle in the game world.
        radius (float): The radius of the circle.
        velocity (pygame.Vector2): The speed and direction of the circle's movement.
    """

    def __init__(self, x: float, y: float, radius: float) -> None:
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface) -> None:
        # sub-classes must override
        pass

    def update(self, dt: int) -> None:
        # sub-classes must override
        pass

    def collide(self, other_shape: pygame.Vector2) -> pygame.Vector2:
        return pygame.Vector2.distance_to(self.position, other_shape.position) <= (
            self.radius + other_shape.radius
        )
