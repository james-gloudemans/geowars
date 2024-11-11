from collections import Counter

import pygame

import conf
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    
    def __init__(self, x: float, y: float) -> "Player":
        super().__init__(x, y, conf.PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.powerups = Counter(conf.POWERUP_KINDS)
        self.powerups["num_shots"] = 1
        
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, (0,255,0), self.triangle(), 2)
        
    def move(self, dt: int, dir: int) -> None:
        direction = pygame.Vector2(0, 1).rotate(dir)
        self.position += direction * conf.PLAYER_SPEED * dt
        if self.position.x > conf.SCREEN_WIDTH - conf.PLAYER_RADIUS:
            self.position.x = conf.SCREEN_WIDTH - conf.PLAYER_RADIUS
        if self.position.x < conf.PLAYER_RADIUS:
            self.position.x = conf.PLAYER_RADIUS
        if self.position.y > conf.SCREEN_HEIGHT - conf.PLAYER_RADIUS:
            self.position.y = conf.SCREEN_HEIGHT - conf.PLAYER_RADIUS
        if self.position.y < conf.PLAYER_RADIUS:
            self.position.y = conf.PLAYER_RADIUS
        
    def shoot(self) -> None:
        shots = [Shot(self.position.x, self.position.y) for _ in range(self.powerups["num_shots"])]
        for shot in shots:
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * conf.PLAYER_SHOOT_SPEED_BASE * (1+self.powerups["shot_speed"]/3)
        match self.powerups["num_shots"]:
            case 1:
                pass
            case 2:
                shots[0].velocity = shots[0].velocity.rotate(5)
                shots[1].velocity = shots[1].velocity.rotate(-5)
            case 3:
                shots[0].velocity = shots[0].velocity.rotate(5)
                shots[2].velocity = shots[2].velocity.rotate(-5)
        self.timer = conf.PLAYER_SHOOT_COOLDOWN_BASE
        
    def update(self, dt: int) -> None:
        self.timer -= dt
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and keys[pygame.K_w]:
            self.move(dt, 135)
        elif keys[pygame.K_d] and keys[pygame.K_w]:
            self.move(dt, 225)
        elif keys[pygame.K_a] and keys[pygame.K_s]:
            self.move(dt, 45)
        elif keys[pygame.K_d] and keys[pygame.K_s]:
            self.move(dt, 315)
        elif keys[pygame.K_a]:
            self.move(dt, 90)
        elif keys[pygame.K_d]:
            self.move(dt, 270)
        elif keys[pygame.K_w]:
            self.move(dt, 180)
        elif keys[pygame.K_s]:
            self.move(dt, 0)
        if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
            self.rotation = 135
            if self.timer <= 0:
                self.shoot()
        elif keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
            self.rotation = 225
            if self.timer <= 0:
                self.shoot()
        elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
            self.rotation = 45
            if self.timer <= 0:
                self.shoot()
        elif keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
            self.rotation = 315
            if self.timer <= 0:
                self.shoot()
        elif keys[pygame.K_LEFT]:
            self.rotation = 90
            if self.timer <= 0:
                self.shoot()
        elif keys[pygame.K_RIGHT]:
            self.rotation = 270
            if self.timer <= 0:
                self.shoot()
        elif keys[pygame.K_UP]:
            self.rotation = 180
            if self.timer <= 0:
                self.shoot()
        elif keys[pygame.K_DOWN]:
            self.rotation = 0
            if self.timer <= 0:
                self.shoot()
        elif keys[pygame.K_ESCAPE]:
            exit()