import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # Pygame 
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Pygame Groups
    updatable  = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable , drawable)
    Asteroid.containers = (asteroids, updatable , drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # Game Loop
    while True:
        # Exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update
        updatable.update(dt)
        for obj in asteroids:
            if obj.collision(player):
                print("Game Over!")
                return

        # Draw
        pygame.Surface.fill(screen, (0,0,0))
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        # FPS Limit
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

