import pygame

import main

class Nicko(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        #nic to l or r
        self.Limage = pygame.image.load("images/nicav.png").convert_alpha()
        self.Rimage = pygame.transform.flip(self.Limage,True,False)
        #new born nic
        self.Limage1 = self.Limage
        self.Rimage1 = self.Rimage
        #nic size
        self.rect = self.Limage.get_rect()
        #nic weigth
        self.size = 1
        #nic moving 1l 2r
        self.direction = 1
        #nic eated
        self.score = 0
        #nic hasn't eat to much
        self.live = True

    def bigger(self):
        if self.size == 3:
            #bigger nic
            self.Limage = pygame.transform.smoothscale(self.Limage1,\
                                                      (int(self.rect.width * 1.4),\
                                                       int(self.rect.height * 1.4)))
            self.Rimage = pygame.transform.flip(self.Limage,True,False)
        elif self.size == 5:
            #biggest nic
            self.Limage = pygame.transform.smoothscale(self.Limage1,\
                                                      (int(self.rect.width * 1.8),\
                                                       int(self.rect.height * 1.8)))
            self.Rimage = pygame.transform.flip(self.Limage,True,False)

    def display_nicko(self,pos1,pos2):
        if pos1[0] - pos2[0] > 0:
            main.screen.blit(self.Limage,self.rect)
            self.direction = 1
        elif pos1[0] - pos2[0] < 0:
            main.screen.blit(self.Rimage,self.rect)
            self.direction = 2
        elif pos1[0] - pos2[0] == 0:
            if self.direction == 1:
                main.screen.blit(self.Limage,self.rect)
            elif self.direction == 2:
                main.screen.blit(self.Rimage,self.rect)
            
