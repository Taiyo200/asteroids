from circleshape import CircleShape
from constants import *
import pygame
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
        
    def draw(self, screen):
        pygame.draw.circle(screen, 
                           (57,255,20), 
                           (self.position.x, self.position.y), 
                           self.radius, 
                           width = 2) 
        
        
    def update(self, dt):
        self.position += (self.velocity * dt)
        
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            new_velocity = 1.2
            split_angle = random.uniform(10,50)
            
            split1 =  pygame.math.Vector2.rotate(self.velocity, split_angle)
            split2 = pygame.math.Vector2.rotate(self.velocity, -split_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = split1 * new_velocity
            asteroid2.velocity = split2 * new_velocity
            self.kill()