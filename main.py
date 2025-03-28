import pygame
from asteroid import *
from constants import *
from circleshape import *
from player import *
from asteroidfield import *

def main():
    print(f"Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init
    
    if pygame.init:
        print("Pygame Initialized")
    else:
        print("Pygame failed")
        
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), vsync=1)
    
    dt = 0
    game_clock = pygame.time.Clock()
    
    drawable_container = pygame.sprite.Group()
    updateable_container = pygame.sprite.Group()
    asteroids_container = pygame.sprite.Group()
    
    Player.containers = (drawable_container, updateable_container)
    Asteroid.containers = (asteroids_container, drawable_container, updateable_container)
    AsteroidField.containers = (updateable_container)
    
    player = Player (x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    
    asteroid_field = AsteroidField()

    
    while(True):
        pygame.Surface.fill(screen, (0,0,0))
        print(dt)
        
        updateable_container.update(dt)
        for drawable in drawable_container:
            drawable.draw(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()
        
        dt = game_clock.tick(60) / 1000
        
        
if __name__ == "__main__":
    main()