from circleshape import CircleShape
import pygame
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface=surface,color="white",center=self.position,radius=self.radius,width=LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rand_angle = random.uniform(20, 50)
        substroid_one_angle = self.velocity.rotate(-rand_angle)
        substroid_two_angle = self.velocity.rotate(rand_angle)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        substroid_one = Asteroid(self.position[0], self.position[1], new_asteroid_radius)
        substroid_one.velocity = substroid_one_angle * 1.2
        substroid_two = Asteroid(self.position[0], self.position[1], new_asteroid_radius)
        substroid_two.velocity = substroid_two_angle * 1.2
