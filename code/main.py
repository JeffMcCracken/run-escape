import sys
import pygame

from states.customize_character import CustomizeCharacter
from game import Game
from settings import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
states = {
    'CUSTOMIZE_CHARACTER': CustomizeCharacter()
}

game = Game(screen, states, 'CUSTOMIZE_CHARACTER')
game.run()

pygame.quit()
sys.exit()