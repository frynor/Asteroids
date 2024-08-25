import pygame
from constants import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color=(0, 0, 0), special_flags=0) 
        pygame.display.flip()

    print("Starting asteroids!")
    printing()


if __name__ == "__main__":
    main()