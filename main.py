import pygame, random
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
        self.player_group=pygame.sprite.LayeredUpdates()

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

        font = pygame.font.SysFont('Comic Sans MS', 30)

        lives_text=font.render(f'Lives: {self.player.lives}', True, (blue))
        score_text = font.render(f'Score: {self.player.score}', True, (blue))
        self.screen.blit(lives_text, (390, 10))
        self.screen.blit(score_text, (10, 10))

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

    def fruitSpawn(self):
        Fruit(self,random.randint(1,14), random.randint(1,2))

    def game_over(self):
        # menuBack = Button(255,350,120,50,"Back to menu",32,white,black, False)

        while self.over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu = False
                    self.running = False

            # mouse_pos = pygame.mouse.get_pos()
            # mouse_pressed = pygame.mouse.get_pressed()

            # if menuBack.is_pressed(mouse_pos, mouse_pressed):
            #     pause=False
            #     self.menu=False
            #     g.mainMenu()


            self.screen.fill(red)
            self.clock.tick(fps)
            pygame.display.update()
        





g=Game()
g.new()

while g.running:
    g.main()

pygame.quit()