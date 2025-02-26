from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape
import pygame
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        angle_1 = self.velocity.rotate(random_angle)
        angle_2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid_split_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_split_2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        asteroid_split_1.velocity = angle_1 * 1.2
        asteroid_split_2.velocity = angle_2 * 1.2