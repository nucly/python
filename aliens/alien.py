import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('images/alien.bmp')
        self.react = self.image.get_rect()

        self.react.x = self.react.width
        self.react.y = self.react.height

        self.x = float(self.react.x)