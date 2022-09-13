import pygame
from settings import *
from spritesheet import Spritesheet
from sprites import Arrow
from timer import Timer

SHIRTS = [
    'basic.png',
    'floral.png',
    'overalls.png',
    'sailor_bow.png',
    'sailor.png',
    'skull.png',
    'spaghetti.png',
    'sporty.png',
    'stripe.png',
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
    'none',
    'hat_cowboy.png',
    'hat_lucky.png',
    'hat_pumpkin_purple.png',
    'hat_pumpkin.png',
    'hat_witch.png',
    'mask_clown_blue.png',
    'mask_clown_red.png',
    'mask_spooky.png',
]

BEARDS = [
    'none',
    ''
]

class CharacterCreation:
    def __init__(self, all_sprites):
        # setup
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font('../font/Habbo.ttf', 40)
        self.margin = 200
        self.all_sprites = all_sprites
        self.arrow_sprites = pygame.sprite.Group()
        self.timer = Timer(200)
        
        # background
        self.width = SCREEN_WIDTH - 100
        self.height = SCREEN_HEIGHT - 100
        self.top = SCREEN_HEIGHT // 2 - self.height // 2
        self.left = SCREEN_WIDTH// 2 - self.width // 2
        self.bg_rect = pygame.Rect(self.left, self.top, self.width, self.height)

        # player skin path and color
        self.skin_color = 0
        self.skin = ['../graphics/character/characters/char_all.png', self.skin_color]

        # All file paths with name
        self.character_assets = {
            'shoe': CharacterAsset('shoe', '../graphics/character/clothes/shoes.png'),
            'eye': CharacterAsset('eye', '../graphics/character/eyes/eyes.png'),
            'shirt': CharacterAsset('shirt', '../graphics/character/clothes/shirts/', SHIRTS),
            'pants': CharacterAsset('pants', '../graphics/character/clothes/pants/', PANTS),
            'hair': CharacterAsset('hair', '../graphics/character/hair/', HAIR),
            'beard': CharacterAsset('beard', '../graphics/character/acc/beard.png', BEARDS),
            'hat': CharacterAsset('hat', '../graphics/character/acc/hats/', HATS)
        }

        # Setup controls
        self.setup()

        
    def preview(self):
        # create base spritesheet
        skin = Spritesheet(self.skin[0], self.skin[1])

        # create asset spritesheets
        assets = []
        asset_offsets = []
        for asset in self.character_assets.values():
            if 'none' in asset.asset_path:
                continue
            assets.append(Spritesheet(asset.asset_path))
            asset_offsets.append(asset.color_shift)

        # Make preview of character and upscale
        preview_surf = skin.get_sprite(0, 0, SPRITESHEET_WIDTH, SPRITESHEET_HEIGHT, assets, asset_offsets)   
        preview_surf = pygame.transform.scale(preview_surf, (preview_surf.get_width() * 2, preview_surf.get_height() * 2))
        preview_rect = preview_surf.get_rect(topleft=(self.left + self.margin // 2 + 70, self.top + 20))
        
        # Display background
        preview_bg_rect = pygame.Rect(preview_rect.x, preview_rect.y, preview_surf.get_width(), preview_surf.get_height())
        pygame.draw.rect(self.display_surface, 'White', preview_bg_rect)

        # Display character
        self.display_surface.blit(preview_surf, preview_rect)

    def options(self):
        options_bg_rect = pygame.Rect(self.left + 100, self.top + 180, 300, 400)
        pygame.draw.rect(self.display_surface, 'White', options_bg_rect)
        num_skipped = 0

        for i, asset in enumerate(self.character_assets.values()):
            if not asset.options:
                num_skipped += 1
                continue
            top = self.top + 180 + (i * 40) - (num_skipped * 40)
            left = self.left + self.margin
            
            text_surf = self.font.render(asset.display_text, False, 'Black')
            text_rect = text_surf.get_rect(topleft=(left, top))
            
            left_arrow = Arrow((left - 58, top), [self.all_sprites, self.arrow_sprites], 'left', asset.name)
            right_arrow = Arrow((left + text_surf.get_width() + 20, top), [self.all_sprites, self.arrow_sprites], 'right', asset.name)
            
            self.display_surface.blit(left_arrow.surf, left_arrow.rect)
            self.display_surface.blit(right_arrow.surf, right_arrow.rect)
            self.display_surface.blit(text_surf, text_rect)

    def setup(self):
        pygame.draw.rect(self.display_surface, 'White', self.bg_rect, 0, 4)
        self.preview()
        self.options()
        

    def input(self):
        for sprite in self.arrow_sprites.sprites():
            if sprite.hitbox.collidepoint(pygame.mouse.get_pos()):
                mouse = pygame.mouse.get_pressed()
                if mouse[0] and not self.timer.active:
                    self.timer.activate()
                    if sprite.direction == 'right':
                        self.press_right(self.character_assets[sprite.name])
                    else:
                        self.press_left(self.character_assets[sprite.name])
                    
                    self.character_assets[sprite.name].update()
                    self.preview()
                    self.options()
            

    def press_right(self, asset):
        if asset.chosen_asset == len(asset.options) - 1:
            asset.chosen_asset = 0
        else:
            asset.chosen_asset += 1

    def press_left(self, asset):
        if asset.chosen_asset == 0:
            asset.chosen_asset = len(asset.options) - 1
        else:
            asset.chosen_asset -= 1

    def update(self):
        self.timer.update()
        self.input()

class CharacterAsset():
    def __init__(self, name, base_path, options=[], chosen_asset=0, color_shift=0):
        self.base_path = base_path
        self.chosen_asset = chosen_asset
        self.options = options
        self.asset_path = self.base_path + self.options[self.chosen_asset] if self.options else self.base_path
        self.color_shift = color_shift
        self.name = name
        self.num_colors = 1 if self.name == 'hat' else 10
        self.display_text = f'{self.name} {self.chosen_asset + 1}' if self.options else self.name

    def update(self):
        self.asset_path = self.base_path + self.options[self.chosen_asset] if self.options else self.base_path
        self.display_text = f'{self.name} {self.chosen_asset + 1}' if self.options else self.name