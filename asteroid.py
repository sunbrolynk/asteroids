import pygame
from circleshape import CircleShape
import random
from constants import *



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        

    ## draw asteroids
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)


    ## update drawn location
    def update(self, dt):
        self.position += self.velocity * dt

    ## method for splitting asteroids into smaller asteroids
    def split(self):
        self.kill()
        random_angle = random.uniform(20, 50)
        new_angle1 = self.velocity.rotate(random_angle)
        new_angle2 = self.velocity.rotate(random_angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = new_angle1 * 1.2
        new_asteroid2.velocity = new_angle2 * 1.2


        ## if small asteroid, kill
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        