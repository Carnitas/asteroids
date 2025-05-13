import pygame
from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS,
    PLAYER_SHOOT_COOLDOWN,
    PLAYER_SHOOT_SPEED,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
)
from shot import Shot


class Player(CircleShape):
    """
    Represents the player's spaceship in the game.

    The Player class handles the player's movement, shooting, and interactions
    with other game objects. It is controlled by user input and can collide with
    asteroids, resulting in a game-over scenario.

    Attributes:
        position (pygame.Vector2): The current position of the player in the game world.
        velocity (pygame.Vector2): The speed and direction of the player's movement.
        radius (float): The radius of the player's spaceship for collision detection.
        lives (int): The number of lives the player has remaining.
    """

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0.0

    def triangle(self) -> list:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> pygame.Rect:
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt: int) -> pygame.Vector2:
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: int) -> None:
        keys = pygame.key.get_pressed()
        self.timer -= dt
        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.shoot()

    def move(self, dt: int) -> pygame.Vector2:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self) -> None:
        bullet = Shot(self.position, self.rotation)
        bullet.velocity = pygame.Vector2(0, 1)
        bullet.velocity = bullet.velocity.rotate(self.rotation)
        bullet.velocity = bullet.velocity * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN
