import pygame
from pygame.locals import *

from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game=game
        self._layer=PLAYER_LAYER
        self.groups=self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x=x*TILESIZE
        self.y=y*TILESIZE
        self.width=TILESIZE
        self.height=TILESIZE

        self.x_change = 225

        self.image = pygame.Surface([self.width,self.height])
        self.image.fill(red)

        self.rect=self.image.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y
    
    def update(self):
        self.movement()

        self.rect.x=self.x_change

    def movement(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x_change-= PLAYER_SPEED

        if keys[pygame.K_RIGHT]:
            self.x_change+=PLAYER_SPEED
            