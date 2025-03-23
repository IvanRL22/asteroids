import random

import pygame.draw

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        # if self.radius > ASTEROID_MIN_RADIUS:
        #     random_angle = random.uniform(20, 50)
        #     new_radius = self.radius - ASTEROID_MIN_RADIUS
        #     new_ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
        #     new_ast_1.velocity = self.velocity.rotate(random_angle) * 1.2
        #     new_ast_2 = Asteroid(self.position.x, self.position.y, new_radius)
        #     new_ast_2.velocity = self.velocity.rotate(-random_angle) * 1.2

