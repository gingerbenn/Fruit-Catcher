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

        self.num = 390

        self.player_speed=5
    
    def update(self):
        self.movement()


        self.rect.x+=self.x_change
        self.collision('x')

        self.x_change=0

        if self.lives <=0:
            pygame.mixer.Sound.play(self.game.minecraftDeath)
            self.game.game_over()
        
        if self.player_speed%5==0:
            self.player_speed+=0.5

        

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
            self.x_change-= self.player_speed

        if keys[pygame.K_RIGHT]:
            self.x_change+=self.player_speed

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
                # self.game.fruit_speed+=0.05
                    

    def movement(self):
        if self.alive:
            self.rect.y += self.game.fruit_speed

        if self.game.player.score%5==0:
            self.game.fruit_speed+=0.01
        

        if self.alive == False:
            pygame.mixer.Sound.play(self.game.minecraftDamage)
            self.game.fruit_count-=1
            self.kill()
            self.game.player.lives-=1
            self.game.fruitSpawn()

        if self.catch == True:
            self.game.fruit_count-=1
            self.kill()
            self.game.player.score+=1
            self.game.fruitSpawn()

class Button:
    def __init__(self,x, y, width, height, content, fontsize, fg, bg):
        self.font = pygame.font.Font('assets/m5x7.ttf',fontsize)
        self.content = content

        self.x = x
        self.y = y
        self.width = width
        self.height = height 

        self.fg = fg
        self.bg = bg

        

        self.image = pygame.Surface((self.width,self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center = (self.width/2,self.height/2))
        self.image.blit(self.text, self.text_rect)

        
        

    
    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            self.bg = blue
            self.image.fill(self.bg)
            self.image.blit(self.text, self.text_rect)
            
            
            if pressed[0]:
                self.image.fill(self.bg)
                self.image.blit(self.text,self.text_rect)
                pygame.time.delay(250)
                return True
            return False
        self.image.fill(self.bg)
        self.image.blit(self.text,self.text_rect)
        self.bg = black
        return False