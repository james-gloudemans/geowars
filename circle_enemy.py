

import math
import random
import pygame
from circleshape import CircleShape
import conf


class BasicCircleEnemy(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, conf.BASIC_CIRCLE_ENEMY_RADIUS)
        angle = random.uniform(0, 2*math.pi)
        self.velocity = pygame.Vector2(math.cos(angle), math.sin(angle)) * conf.BASIC_CIRCLE_ENEMY_SPEED
        self.score = conf.BASIC_CIRCLE_ENEMY_SCORE

    def draw(self, screen: pygame.Surface) -> None:
        if self.position.x > conf.SCREEN_WIDTH - conf.BASIC_CIRCLE_ENEMY_RADIUS:
            self.velocity.x = -self.velocity.x
        if self.position.x < conf.BASIC_CIRCLE_ENEMY_RADIUS:
            self.velocity.x = -self.velocity.x
        if self.position.y > conf.SCREEN_HEIGHT - conf.BASIC_CIRCLE_ENEMY_RADIUS:
            self.velocity.y = -self.velocity.y
        if self.position.y < conf.BASIC_CIRCLE_ENEMY_RADIUS:
            self.velocity.y = -self.velocity.y
        pygame.draw.circle(screen, conf.BASIC_CIRCLE_ENEMY_COLOR, self.position, self.radius, 2)

    def update(self, dt: int) -> None:
        self.position += self.velocity * dt

    def die(self) -> None:
        self.kill()
        