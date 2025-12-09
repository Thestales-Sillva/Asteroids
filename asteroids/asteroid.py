from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if (self.radius <= ASTEROID_MIN_RADIUS):
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)

            #Asteroid 1
            one_velocity = self.velocity.rotate(random_angle)
            asteroid_one = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
            asteroid_one.velocity = one_velocity * 1.2

            #Asteroid 2
            two_velocity = self.velocity.rotate(-random_angle)
            asteroid_two = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
            asteroid_two.velocity = two_velocity * 1.2
