

import pygame
from circleshape import CircleShape
import conf


class Powerup(CircleShape):

    color_map = {conf.POWERUP_KINDS[0]: (255,100,100), conf.POWERUP_KINDS[1]: (100,255,100)}
    def __init__(self, x: float, y: float, kind):
        super().__init__(x, y, conf.POWERUP_RADIUS)
        self.kind = kind
        self.color = self.color_map[kind]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, self.color, self.position, self.radius, 2)

    def update(self, dt: int) -> None:
        self.position += self.velocity * dt