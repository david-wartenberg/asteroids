import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    clock.tick(60)
    dt = 0.0
    
    updatable   = pygame.sprite.Group()
    drawable    = pygame.sprite.Group()
    asteroids   = pygame.sprite.Group()
    shots       = pygame.sprite.Group()

    Player.containers           = (updatable, drawable)
    Asteroid.containers         = (asteroids, updatable, drawable)
    AsteroidField.containers    = updatable
    Shot.containers             = (shots, drawable, updatable)

    field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2) 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)


    score = 0

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        
        for a in asteroids:
            if a.collides_with(player):
                log_event("player_hit")
                print("Game Over!")
                pygame.quit()
                sys.exit()
            for s in shots:
                if a.collides_with(s):
                    log_event("asteroid_shot")
                    score += 1
                    a.split()
                    s.kill()
        for d in drawable:
            d.draw(screen)

        if pygame.font:
            font = pygame.font.Font(None, 64)
            text = font.render(f"Score: {score}", True, "white")
            textpos = text.get_rect(centerx=SCREEN_WIDTH / 2, y=10)
            screen.blit(text, textpos)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()
