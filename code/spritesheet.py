import pygame
from settings import *

class Spritesheet:
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert_alpha()
        self.sheet_width = self.sprite_sheet.get_width()
        self.sheet_height = self.sprite_sheet.get_height()

    def get_sprite(self, x, y, w, h):
        sprite = pygame.Surface((w,h))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sprite_sheet, (0,0), (x, y, w, h))
        sprite = pygame.transform.scale(sprite, (TILE_SIZE, TILE_SIZE))
        return sprite

    def get_frames(self, end_x, end_y, w, h):
        frame_cols = int(end_x / w)
        frame_rows = int(end_y / h)

        frames = []

        for row in range(frame_rows):
            for col in range(frame_cols):
                frame = self.get_sprite(col*w, row*h, w, h)
                frames.append(frame)

        return frames