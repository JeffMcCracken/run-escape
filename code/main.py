import pygame, sys, time

from settings import *
from player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.canvas = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Run Escape')
        self.clock = pygame.time.Clock()
        all_sprites = pygame.sprite.Group()
        self.player = Player((20, 20), all_sprites)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            dt = self.clock.tick() / 1000
            self.canvas.fill((255, 255, 255))
            self.canvas.blit(self.player.image, self.player.rect)
            self.screen.blit(self.canvas, (0,0))
            self.player.update(dt)
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()
