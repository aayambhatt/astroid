import pygame
from constants import *
from player import Player


def main():
    pygame.init() # Initialize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Create game window
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    clock = pygame.time.Clock()  # Regulates FPS
    dt = 0  # Delta time (time between frames)
    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit game loop
        
        player.update(dt) 
            
        screen.fill((0,0,0)) # set screen to solid black
        player.draw(screen) # Draw the player

        pygame.display.flip() # Refresh the screen

        dt = clock.tick(60) / 1000  # Limit to 60 FPS, get delta time in seconds

        

        

if __name__ == "__main__":
    main()