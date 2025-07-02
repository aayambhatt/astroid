import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()  # Always destroy the current asteroid

        if self.radius <= ASTEROID_MIN_RADIUS:
            return  # Too small to split further

    # New radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

    # Generate a random angle between 20–50 degrees
        random_angle = random.uniform(20, 50)

    # Create 2 new velocity vectors (opposite directions)
        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2

    # Spawn 2 new asteroids at the same position
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity1
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity2

