from circleshape import CircleShape
from logger import log_event
import random
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x: float, y:float, radius:float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            split_angle = random.uniform(20,50)
            asteroid1 = self.velocity.rotate(split_angle)
            asteroid2 = self.velocity.rotate(-split_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new1 = Asteroid(asteroid1[0], asteroid1[1], new_radius)
            new1.velocity = new1.velocity * 1.15
            new2 = Asteroid(asteroid2[0], asteroid2[1], new_radius)
            new2.velocity = new2.velocity * 1.15
