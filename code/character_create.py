import pygame
from settings import *

class CharacterCreation:
    def __init__(self):
        # setup
        self.display_surface = pygame.display.get_surface()
        
        # background:
        self.width = SCREEN_WIDTH - 100
        self.height = SCREEN_HEIGHT - 100
        self.top = SCREEN_HEIGHT // 2 - self.height // 2
        self.left = SCREEN_WIDTH// 2 - self.width // 2
        self.bg_rect = pygame.Rect(self.left, self.top, self.width, self.height)
        
    def update(self):
        pygame.draw.rect(self.display_surface, 'White', self.bg_rect, 0, 4)
        