import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots =pygame.sprite.Group()
    Shot.containers = (updatable, drawable, shots)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    clock = pygame.time.Clock()
    dt = 0.0
    score = 0
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()
        for event in pygame.event.get():
            dt = clock.tick(120) / 1000
            if event.type == pygame.QUIT:
                return
        if dt > 0.05:
            print("slow frame", dt)
            print(len(asteroids))
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player) == True:
                log_event("player_hit")
                print("Game Over!")
                print(f"You Scored {score} Points!")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot) == True:
                    log_event("asteroid_shot")
                    score += 100
                    asteroid.split()
                    shot.kill()
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()




if __name__ == "__main__":
    main()
