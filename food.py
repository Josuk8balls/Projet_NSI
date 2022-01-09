import pygame
from random import *

import main

#food
class Food(pygame.sprite.Sprite):
    def __init__(self,bg_size,food_image,size,speed,num):  
        pygame.sprite.Sprite.__init__(self)
        
        #food to left
        self.image = pygame.image.load(food_image).convert_alpha()
        #image consideré mask
        self.mask = pygame.mask.from_surface(self.image)
        
        #image l and r
        self.Limage = self.image
        self.Rimage = pygame.transform.flip(self.Limage,True,False)
        #rect of food
        self.rect = self.image.get_rect()
        
        #food size
        self.size = size
        #food uneated
        self.uneated = True
        #food speed
        self.speed = speed
        
        #food deplacement
        self.width, self.height = bg_size[0], bg_size[1]

        #food forward(1:l  2:r)
        self.direction = num

        #food position init
        self.rect.center = (randint(850, 5 * self.width),randint(0, self.height-self.rect.height))if self.direction==1 else (randint(-5 * self.width, 0),randint(0, self.height-self.rect.height))

    def reset(self):
        #if r : reset l
        if self.direction == 1:
            self.rect.center = (randint(850, 5 * self.width),randint(0, self.height-self.rect.height))
            self.direction == 2
        #if l : reset r
        elif self.direction == 2:
            self.rect.center = (randint(-5 * self.width, 0),randint(0, self.height-self.rect.height))
            self.direction == 1
            
    def move(self):
        # go to l
        if self.direction == 1 and self.rect.right >= 0:
            self.rect.left -= self.speed
        elif self.direction ==1 and self.rect.right <= 0:
            self.reset()
        # go to r
        if self.direction == 2 and self.rect.left <= self.width:
            self.rect.left += self.speed
        elif self.direction ==2 and self.rect.left >= self.width:
            self.reset()

    def display_food(self):
        # food look l
        if self.direction == 1:
            self.image = self.Limage
        # food look r
        elif self.direction == 2: 
            self.image = self.Rimage
        main.screen.blit(self.image,self.rect)

#snacks
class smallFood(Food):
    pass

#realstuff
class midFood(Food):
    pass

#meal
class bigFood(Food):
    pass

#ITSFKINGRAWWW
class Boss(pygame.sprite.Sprite):
    def __init__(self,bg_size,food_image,num):  
        pygame.sprite.Sprite.__init__(self)
        
        # boss to l
        self.image = pygame.image.load(food_image).convert_alpha()
        #将非透明部分标记为mask
        self.mask = pygame.mask.from_surface(self.image)
        
        # l and r
        self.Limage = self.image
        self.Rimage = pygame.transform.flip(self.Limage,True,False)
        #获取鱼矩形区域
        self.rect = self.image.get_rect()
        
        # boss size
        self.size = 6
        # boss speeeeeeeeeeeeeeeeed
        self.speed = 5
        
        # boss zone
        self.width, self.height = bg_size[0], bg_size[1]

        # boss direction 1=l 2=r
        self.direction = num

        #boss position
        self.rect.center = ( 15 * self.width,randint(0, self.height-self.rect.height)) \
                            if self.direction==1 \
                            else (-15 * self.width,randint(0, self.height-self.rect.height))
            
    def reset(self):
            #if r : l
            if self.direction == 1:
                self.rect.center = (15 * self.width, randint(0, self.height-self.rect.height))
                self.direction == 2
            #if l : r
            elif self.direction == 2:
                self.rect.center = (-15 * self.width, randint(0, self.height-self.rect.height))
                self.direction == 1
            

    def move(self):
        #go to l
        if self.direction == 1 and self.rect.right >= 0:
            self.rect.left -= self.speed
        elif self.direction ==1 and self.rect.right < 0:
            self.reset()
        #go to r
        if self.direction == 2 and self.rect.left <= self.width:
            self.rect.left += self.speed
        elif self.direction ==2 and self.rect.left > self.width:
            self.reset()

    def display_food(self):
        #look l
        if self.direction == 1:
            self.image = self.Limage
        #look r
        elif self.direction == 2: 
            self.image = self.Rimage
        main.screen.blit(self.image,self.rect)
        
        
        
        
        
