import pygame
from settings import *

class Arrow(pygame.sprite.Sprite):
    def __init__(self, pos, groups, direction, name):
        super().__init__(groups)
        self.direction = direction
        self.name = name
        self.surf = pygame.image.load(f'../graphics/icons/arrow_{self.direction}.png').convert_alpha()
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect(topleft=pos)
        self.hitbox = self.rect.copy()
        self.mask = pygame.mask.from_surface(self.surf)

class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load(f'../graphics/icons/cursor.png').convert_alpha()
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect(topleft=(0,0))
        self.mask = pygame.mask.from_surface(self.surf)

    def update(self):
        if pygame.mouse.get_pos():
            self.rect.topleft = pygame.mouse.get_pos()
        