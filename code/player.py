import pygame
from settings import *
from spritesheet import Spritesheet

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.spritesheet = Spritesheet('../graphics/character/characters/char1.png')
        self.frames = self.spritesheet.get_frames(
            self.spritesheet.sheet_width,
            SPRITESHEET_SIZE,
            SPRITESHEET_SIZE,
            SPRITESHEET_SIZE
        )
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

    def cycle_frames(self, dt):
        self.frame_index += dt * 6
        if self.frame_index > len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self, dt):
        self.cycle_frames(dt)

        
