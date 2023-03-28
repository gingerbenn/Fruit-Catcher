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

        self.over=True
        self.running=True
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
        Fruit(self,random.randint(2,13), random.randint(-3,-1))

    def game_over(self):
        menuBack = Button(175,275,175,50,"Back to menu",24,white,black)
        self.playing = False

        while self.over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.over=False
                    self.playing=False
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if menuBack.is_pressed(mouse_pos, mouse_pressed):
                self.menu=True
                self.playing=True
                self.main_menu()



            font = pygame.font.SysFont('Comic Sans MS', 30)
            self.screen.fill(red)
            dead_text = font.render('dead', True, (blue))
            self.screen.blit(dead_text, (390,10))
            self.screen.blit(menuBack.image, menuBack.rect)
            self.clock.tick(fps)
            pygame.display.update()

    def main_menu(self):
        startButton = Button(175,275,175,50,"Start!",24,white,black)
        menu=True

        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu=False
                    self.playing=False
                    self.running = False
        
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if startButton.is_pressed(mouse_pos, mouse_pressed):
                print('works')
                menu = False
                # print(self.player.lives)

            self.screen.fill(red)
            self.screen.blit(startButton.image, startButton.rect)
            self.clock.tick(fps)
            pygame.display.update()
        
                
        




def startgame():
    g=Game()
    g.main_menu()
    g.new()

    while g.running:
        g.main()
    #g.game_over()

    pygame.quit()

startgame()