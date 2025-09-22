from circleshape import CircleShape
from constants import *
import pygame 


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.rotation = 0
        self.radius = SHOT_RADIUS

    ## draw asteroids
    # python
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, 2)


    def update(self, dt):
        self.position += self.velocity * dt


        