import pygame
from constants import *
from player import Player

def main():
    # Pygame 
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    # Pygame Groups
    updatable  = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable , drawable)
    
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game Loop
    while True:
        # Exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update
        updatable.update(dt)
        
        # Draw
        pygame.Surface.fill(screen, (0,0,0))
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        # FPS Limit
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

