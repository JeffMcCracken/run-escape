import pygame

from .base import BaseState

class CustomizeCharacter(BaseState):
    def __init__(self):
        super().__init__()
        self.title = self.font.render("Customize Character", False, 'White')
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)

    def draw(self, surface):
        surface.fill(pygame.Color("black"))
        surface.blit(self.title, self.title_rect)
