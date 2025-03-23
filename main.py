# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys

import pygame

import constants
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player


def main():
    print('Starting Asteroids!')
    print('Screen width:', constants.SCREEN_WIDTH)
    print('Screen height:', constants.SCREEN_HEIGHT)

    pygame.init()
    game_clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables, asteroids)
    AsteroidField.containers = updatables

    player_ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # Game loop
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('black')
        delta_t = game_clock.tick(60) / 1000

        for u in updatables:
            u.update(delta_t)

        for d in drawables:
            d.draw(screen)

        for a in asteroids:
            if a.is_colliding(player_ship):
                print('Game over!')
                sys.exit(0)

        # This should work according to the project instructions, why doesn't it?
        # updatables.update(delta_t)
        # drawables.draw(screen)

        pygame.display.flip()



if __name__ == "__main__":
    main()