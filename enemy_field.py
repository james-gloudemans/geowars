

import random
import pygame

from circle_enemy import BasicCircleEnemy
import conf

class EnemyField(pygame.sprite.Sprite):
    spawn_points: list[pygame.Vector2] = [
        pygame.Vector2(conf.SPAWN_PADDING, conf.SCREEN_HEIGHT - conf.SPAWN_PADDING),
        pygame.Vector2(conf.SPAWN_PADDING, conf.SPAWN_PADDING),
        pygame.Vector2(conf.SCREEN_WIDTH - conf.SPAWN_PADDING, conf.SPAWN_PADDING),
        pygame.Vector2(conf.SCREEN_WIDTH - conf.SPAWN_PADDING, conf.SCREEN_HEIGHT - conf.SPAWN_PADDING),
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0
        self.group_spawn_timer = 0.0
        self.group_counter = 0
        self.spawn_point = random.choice(self.spawn_points)



    def update(self, dt: int) -> None:
        self.spawn_timer += dt
        if self.spawn_timer > conf.ENEMY_GROUP_SPAWN_INTERVAL:
            self.group_spawn_timer += dt
            if self.group_spawn_timer > conf.ENEMY_SPAWN_INTERVAL:
                BasicCircleEnemy(self.spawn_point.x, self.spawn_point.y)
                self.group_counter += 1
                self.group_spawn_timer = 0.0
                if self.group_counter > conf.ENEMY_GROUP_SIZE:
                    self.spawn_timer = 0
                    self.group_counter = 0
                    self.spawn_point = random.choice(self.spawn_points)


