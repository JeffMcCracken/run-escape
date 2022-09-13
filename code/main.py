import pygame, sys

from settings import *
from player import Player
from character_create import CharacterCreation

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.canvas = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Run Escape')
        self.clock = pygame.time.Clock()
        all_sprites = pygame.sprite.Group()
        self.player = Player((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), all_sprites)
        self.character_creation = CharacterCreation()
        self.state = 'character_create'
        
    def character_create(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RETURN]:
            self.state = 'main_game'
        
        self.character_creation.update()
              
                
    def main_game(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_ESCAPE]:
            self.state = 'character_create'
        
        self.canvas.fill((0, 0, 0))
        self.canvas.blit(self.player.image, self.player.rect)
        self.screen.blit(self.canvas, (0,0))
        self.player.update(dt)
        

    def run(self):
        while True:
            dt = self.clock.tick() / 1000
            
            if self.state == 'character_create':
                self.character_create()
            elif self.state == 'main_game':
                self.main_game(dt)

            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()
