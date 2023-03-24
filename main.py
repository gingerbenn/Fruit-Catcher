import pygame
import pandas as pd
from config import *
from objects import *

class Game:
    def __init__(self):
        pygame.init()

        self.bg=pygame.image.load('assets/test background.png')
        self.bg=pygame.transform.scale(self.bg,(win_width,win_height))

        self.screen=pygame.display.set_caption('fruit catcher™')
        self.screen=pygame.display.set_mode((win_width, win_height))
        self.clock=pygame.time.Clock()

        self.running=True

    def new(self):
        self.playing=True

        self.all_sprites=pygame.sprite.LayeredUpdates()
        self.blocks=pygame.sprite.LayeredUpdates()
        self.fruits=pygame.sprite.LayeredUpdates()

        self.createTilemap()

    def events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.playing=False
                self.running=False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.blit(self.bg,(0,0))
        self.all_sprites.draw(self.screen)
        self.clock.tick(fps)
        pygame.display.update()

    def main(self):
        while self.playing:
            self.draw()
            self.events()
            self.update()
        self.running=False
    
    def createTilemap(self):
        for i,row in enumerate(tilemap):
            for j,column in enumerate(row):
                if column=='B':
                    Block(self,j,i)
                if column =='P':
                    self.player = Player(self,j,i)
                if column=='F':
                    Fruit(self,j,i)

g=Game()
g.new()

while g.running:
    g.main()

pygame.quit()