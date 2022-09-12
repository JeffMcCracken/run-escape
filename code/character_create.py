import pygame
from settings import *
from spritesheet import Spritesheet

SHIRTS = [
    'basic.png',
    'floral.png',
    'overalls.png',
    'sailor_bow.png',
    'sailor.png',
    'skull.png',
    'spaghetti.png',
    'sporty.png',
    'string.png',
    'suit.png'
]

PANTS = [
    'pants.png',
    'pants_suit.png',
    'skirt.png'
]

HAIR = [
    'bob.png',
    'braids.png',
    'buzzcut.png',
    'curly.png',
    'emo.png',
    'extra_long_skirt.png',
    'extra_long.png',
    'french_curl.png',
    'gentleman.png',
    'long_straight_skirt.png',
    'long_straight.png',
    'midiwave.png',
    'ponytail.png',
    'spacebuns.png',
    'wavy.png'
]

HATS = [
    'hat_cowboy.png',
    'hat_lucky.png',
    'hat_pumpkin_purple.png',
    'hat_pumpkin.png',
    'hat_witch.png',
    'hat_clown_blue.png',
    'hat_clown_red.png',
    'hat_spooky.png',
]

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

        # player skin path and color
        self.skin = ['../graphics/character/characters/char_all.png', 0]

        # player asset paths
        self.shoe_path = '../graphics/character/clothes/shoes.png'
        self.eye_path = '../graphics/character/eyes/eyes.png'
        self.beard_path = '../graphics/character/acc/beard.png'
        self.shirt_path = '../graphics/character/clothes/shirts/'
        self.pants_path = '../graphics/character/clothes/pants/'
        self.hair_path = '../graphics/character/hair/'
        self.hat_path = '../graphics/character/acc/hats/'

        # default chosen assets
        self.shirt = SHIRTS[0]
        self.pants = PANTS[0]
        self.hair = HAIR[0]
        self.hat = HATS[0]

        # All file paths with chose, color
        self.character_assets = [
            [self.shoe_path, 0],
            [self.eye_path, 0],
            [self.beard_path, 0],
            [self.shirt_path + self.shirt, 0],
            [self.pants_path + self.pants, 0],
            [self.hair_path + self.hair, 0],
            [self.hat_path + self.hat, 0]
        ]

        
    def preview(self):
        # create base spritesheet
        skin = Spritesheet(self.skin[0], self.skin[1])

        # create asset spritesheets
        assets = []
        for asset in self.character_assets:
            assets.append([Spritesheet(asset[0]), asset[1]])

        preview = skin.get_sprite(0, 0, SPRITESHEET_WIDTH, SPRITESHEET_HEIGHT, assets[0], assets[1])
        self.display_surface.blit(preview, (0,0))

    def update(self):
        pygame.draw.rect(self.display_surface, 'White', self.bg_rect, 0, 4)
        self.preview()
        