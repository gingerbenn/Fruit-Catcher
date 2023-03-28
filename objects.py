import pygame
from pygame.locals import *

from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game=game
        self._layer=PLAYER_LAYER
        self.groups=self.game.all_sprites, self.game.player_group
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x=x*TILESIZE
        self.y=y*TILESIZE
        self.width=TILESIZE*2
        self.height=TILESIZE

        self.x_change = 0

        self.image = pygame.Surface([self.width,self.height])
        self.image.fill(red)

        self.rect=self.image.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y

        self.score=0
        self.lives=3
    
    def update(self):
        self.movement()

        self.rect.x+=self.x_change
        self.collision('x')

        self.x_change=0

        self.over = True

        if self.lives <=0:
            self.game.over=True
            self.game.game_over()

        

    def collision(self,direction):
        self.collide_blocks(direction)

    def collide_blocks(self,direction):
        if direction=='x':
            hits=pygame.sprite.spritecollide(self,self.game.blocks,False)
            if hits:
                if self.x_change>0:
                    self.rect.x=hits[0].rect.left-self.rect.width
                if self.x_change<0:
                    self.rect.x=hits[0].rect.right

    def movement(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x_change-= PLAYER_SPEED

        if keys[pygame.K_RIGHT]:
            self.x_change+=PLAYER_SPEED

class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game=game
        self._layer=block_layer
        self.groups=self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self,self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = pygame.Surface([self.width,self.height])
        self.image.fill(blue)
        self.image.set_colorkey(blue)

        self.rect=self.image.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y

        

class Fruit(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = fruit_layer
        self.groups = self.game.all_sprites, self.game.fruits
        pygame.sprite.Sprite.__init__(self,self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(green)

        self.rect = self.image.get_rect()
        self.rect.y = self.y
        self.rect.x = self.x

        self.alive = True
        self.catch=False

        self.y_change = 0

    def update(self):
        self.movement()

        self.rect.y += self.y_change
        self.collide_floor('y')
        self.collide_player('y')

        self.y_change = 0

    

    def collide_floor(self,direction):
        if direction == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                self.alive = False

    def collide_player(self,direction):
        if direction == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.player_group, False)
            if hits:
                self.catch = True
                    

    def movement(self):
        if self.alive:
            self.rect.y += fruit_speed

        if self.alive == False:
            self.kill()
            self.game.player.lives-=1
            self.game.fruitSpawn()
            print(self.game.player.lives)

        if self.catch == True:
            self.kill()
            self.game.player.score+=1
            self.game.fruitSpawn()
            print(self.game.player.score)