import pygame

from circle_enemy import BasicCircleEnemy
import conf
from enemy_field import EnemyField
from player import Player
from shot import Shot

def main():
    print("Starting GeoWars!")
    print(f"Screen width: {conf.SCREEN_WIDTH}")
    print(f"Screen height: {conf.SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((conf.SCREEN_WIDTH, conf.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt: int = 0
    score: int = 0
    lives: int = 3
    game_font = pygame.font.SysFont('Comic Sans MS', 30)
    score_text = game_font.render(f'Score: {score}', False, (255,255,255))
    lives_text = game_font.render(f'Lives: {lives}', False, (255,255,255))

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Shot.containers = (shots, updatables, drawables)
    EnemyField.containers = (updatables)
    BasicCircleEnemy.containers = (enemies, updatables, drawables)

    player = Player(conf.SCREEN_WIDTH/2, conf.SCREEN_HEIGHT/2)
    enemy_spawner = EnemyField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for obj in updatables:
            obj.update(dt)
        for obj in drawables:
            obj.draw(screen)
        for enemy in enemies:
            if enemy.collides_with(player):
                lives -= 1
                if lives == 0:
                    print("Game over!")
                    exit()
                else:
                    for enemy in enemies:
                        enemy.kill()
                    for shot in shots:
                        shot.kill()
                    lives_text = game_font.render(f'Lives: {lives}', False, (255,255,255))
                    player.kill()
                    player = Player(conf.SCREEN_WIDTH/2, conf.SCREEN_HEIGHT/2)
                    enemy_spawner.kill()
                    enemy_spawner = EnemyField()
                    break
            for shot in shots:
                if enemy.collides_with(shot):
                    score += enemy.score
                    score_text = game_font.render(f'Score: {score}', False, (255,255,255))
                    enemy.die()
                    shot.kill()

        screen.blit(score_text, (conf.TEXT_PADDING, 0))
        screen.blit(lives_text, (conf.SCREEN_WIDTH - (lives_text.get_width() + conf.TEXT_PADDING), 0))
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()
