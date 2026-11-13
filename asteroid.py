from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface=surface,color="white",center=self.position,radius=self.radius,width=LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

