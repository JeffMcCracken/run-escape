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
        