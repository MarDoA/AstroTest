import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        n_radius = self.radius - ASTEROID_MIN_RADIUS
        n_astero1 = Asteroid(self.position.x, self.position.y, n_radius)
        n_astero2 = Asteroid(self.position.x, self.position.y, n_radius)
        n_astero1.velocity = self.velocity.rotate(random_angle) * 1.2
        n_astero2.velocity = self.velocity.rotate(-random_angle) * 1.2

        

    def update(self, dt):
        self.position += (self.velocity * dt)