import pygame

# Base class for circle-ish game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, radius: float) -> "CircleShape":
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface):
        return NotImplemented

    def update(self, dt: int):
        return NotImplemented
    
    def collides_with(self, other: "CircleShape") -> bool:
        return self.position.distance_to(other.position) <= self.radius + other.radius