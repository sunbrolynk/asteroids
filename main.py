# import modules from other files
import pygame
import sys
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
    
    ## initilization & global variables
    print("Starting Asteroids!\nScreen width: 1280\nScreen height: 720")
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        

        ## create black background
        screen.fill("black")
        
        ## player and player functions
        updatable.update(dt)
        for asteroid in asteroids:
            if player.check_collisions(asteroid):
                print("Game Over!")
                sys.exit()
            

        for i in drawable:
            i.draw(screen)



        ## refresh screen
        pygame.display.flip()
    
    
        #  limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
