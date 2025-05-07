import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH


def main() -> None:
    pygame.display.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.display.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
