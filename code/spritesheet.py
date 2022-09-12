import pygame
from settings import *

class Spritesheet:
    def __init__(self, filename, offset=0):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert_alpha()
        self.sheet_width = self.sprite_sheet.get_width()
        self.sheet_height = self.sprite_sheet.get_height()
        self.color_offset = offset

    def get_sprite(self, x, y, w, h, spritesheets = None, spritesheet_col_shifts = None):
        sprite = pygame.Surface((w,h))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sprite_sheet, (0,0), (x, y, w, h))
        if spritesheets:
            for i, spritesheet in enumerate(spritesheets):
                sprite.blit(spritesheet.sprite_sheet, (0,0), (x + spritesheet_col_shifts[i], y, w, h))
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
    
    def get_frames_row(self, row, frame_count, max_frames, w, h, spritesheets = None):
        frames = []
        spritesheet_col_shifts = []
        color_col_shift = self.color_offset * max_frames * w
        if spritesheets:
            for spritesheet in spritesheets:
                spritesheet_col_shifts.append(spritesheet.color_offset * 8 * w - color_col_shift)


        for col in range(frame_count):
            frame = self.get_sprite(col*w + color_col_shift, row*h, w, h, spritesheets, spritesheet_col_shifts)
            frames.append(frame)

        return frames