import pygame
from settings import *
from spritesheet import Spritesheet

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        # setup
        self.frames = {}
        self.frame_index = 0
        self.status = 'down_idle'
        self.animation_speed = 8

        # character customization
        self.spritesheet = Spritesheet('../graphics/character/characters/char_all.png')
        self.shirt = Spritesheet('../graphics/character/clothes/shirts/floral.png')
        self.pants = Spritesheet('../graphics/character/clothes/pants/pants.png')
        self.hair = Spritesheet('../graphics/character/hair/curly.png', 11)
        self.shoes = Spritesheet('../graphics/character/clothes/shoes.png')
        self.eyes = Spritesheet('../graphics/character/eyes/eyes.png')
        self.acc = Spritesheet('../graphics/character/acc/beard.png')
        self.customizations = [self.shirt, self.pants, self.hair, self.shoes, self.eyes, self.acc]
        self.setup_frames()

        # set image and pos
        self.image = self.frames[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)

        # movement
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

        # groups
        self.groups = groups 

    def setup_frames(self):
        for animation in CHARACTER_ANIMATIONS:
            row = CHARACTER_ANIMATIONS[animation][0]
            frame_count = CHARACTER_ANIMATIONS[animation][1]
            max_frames = CHARACTER_ANIMATIONS[animation][2]

            self.frames[animation] = self.spritesheet.get_frames_row(
                row, frame_count, max_frames, SPRITESHEET_WIDTH, SPRITESHEET_HEIGHT, self.customizations
            )

    def input(self):
        keys = pygame.key.get_pressed()

        # horizontal movement
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
            self.frame = 0
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
            self.frame = 0
        else:
            self.direction.x = 0

        # vertical movement
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'
            self.frame = 0
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
            self.frame = 0
        else:
            self.direction.y = 0
    
    def move(self, dt):
        # normalize the vector for diagonal movement
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        # horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = round(self.pos.x)

        # vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = round(self.pos.y)

    def get_status(self):
        if self.direction.magnitude() == 0:
            self.status = self.status.split('_')[0] + '_idle'
                
    def animate(self, dt):
        self.frame_index += self.animation_speed * dt
        if self.frame_index >= len(self.frames[self.status]):
            self.frame_index = 0
        self.image = self.frames[self.status][int(self.frame_index)]

    def update(self, dt):
        self.input()
        self.get_status()

        self.move(dt)
        self.animate(dt)

        
