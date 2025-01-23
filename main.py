import pygame
from constants import *
from player import *
from astroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    Asteroid.containers =(asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    asterofield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for ob in updatable:
            ob.update(dt)
        
        for ob in asteroids:
            if ob.is_collide(player):
                print("Game over!")
                return

        screen.fill((0,0,0))
        for ob in drawable:
            ob.draw(screen)

        pygame.display.flip()

        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()