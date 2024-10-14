import pygame

import conf
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
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Shot.containers = (shots, updatables, drawables)

    player = Player(conf.SCREEN_WIDTH/2, conf.SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for obj in updatables:
            obj.update(dt)
        for obj in drawables:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()
