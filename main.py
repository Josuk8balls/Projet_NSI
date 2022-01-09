import pygame
import sys
import traceback
from pygame.locals import *
from random import *

import nicko
import food

pygame.init()
bg_size = width,height = 850,600
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("nicaubuffet")
clock = pygame.time.Clock()

#soul 
pygame.mixer.music.load("music/bg_music.mp3")
pygame.mixer.music.set_volume(0.3)
die_sound = pygame.mixer.Sound("music/die.mp3")
die_sound.set_volume(0.5)
eat_sound = pygame.mixer.Sound("music/eat.wav")
eat_sound.set_volume(0.3)




#saving foods
foods = pygame.sprite.Group()
#list for bigdaddy
boss_stat = []
#imgs
sfood_img = ["images/coca.png", "images/burger.png"]
mfood_img = ["images/frites.png", "images/icecream.png"]
bfood_img = ["images/chicken.png", "images/hotdog.png"]
boss_img = ["images/gr.png", "images/rock.png"]

#cooking
def init_foods():
    #12 snacks any time
    for img in sfood_img:
        for i in range(12):
            num = randint(1,2)
            food_ = food.Food(bg_size,img,0,3,num)
            foods.add(food_)
    #4 dishes any time
    for img in mfood_img:
        for i in range(4):
            num = randint(1,2)
            food_ = food.Food(bg_size,img,2,3,num)
            foods.add(food_)
    #2 meals any time
    for img in bfood_img:
        for i in range(4):
            num = randint(1,2)
            food_ = food.Food(bg_size,img,4,3,num)
            foods.add(food_)
            
    #STOPEATINGNICKO
    for img in boss_img:
        num = randint(1,2)
        food_ = food.Boss(bg_size,img,num)
        boss_stat.append(food_)
    

#pause
unpause_img = "images/unpause.png"
pause_img = "images/pause.png"
#suppose to draw pause
def load_icon(img,rect):
    image = pygame.image.load(img).convert_alpha()
    screen.blit(image,rect)
#draw GG
def load_text(content,size,color,position):
    font = pygame.font.SysFont("kaiti",size)
    text = font.render(content, True, color)
    screen.blit(text,position) 


#draw foods
def load_foods():
    for food_ in foods:
        if food_.uneated:
            food_.move()
            food_.display_food()
        else:
            food_.reset()
            food_.uneated=True
            
    for food_ in boss_stat:
        food_.move()
        food_.display_food()
        

#big boss hitting nicko
def boss_collide(nic):
    for food_ in boss_stat:
        #all enemies
        array = pygame.sprite.spritecollide(food_,foods,False,pygame.sprite.collide_mask)
        if array:
            for i in array:
                i.live = False
        #its now personnal
        if pygame.sprite.collide_rect_ratio(0.8)(food_,nic):
            nic.live = False


#nicko parry
def nicko_collide(nic):
    for food_ in foods:
        if pygame.sprite.collide_rect_ratio(0.8)(food_,nic):
            #nicko eating
            if nic.size > food_.size:
                eat_sound.play()
                food_.uneated =  False
                #yummy
                if food_.size == 0:
                    nic.score += 20
                elif food_.size == 2:
                    nic.score += 20
                elif food_.size == 4:
                    nic.score += 40
            #nicko get hit
            else:
                nic.live = False
         
                
#"let's go find some frites".jpg
def elude_pursue(nic):
    for food_ in foods:
        #"here's nicko"
        if 0 < food_.rect.left < width - food_.rect.width and nic.rect.left-100 < food_.rect.left < nic.rect.left+100:
            #"no nicko, no (>_<) "
            if food_.size < nic.size:
                if int(abs(food_.rect.bottom - nic.rect.top)) < 40:
                    if food_.direction != nic.direction:
                        food_.direction = nic.direction
                    food_.rect.bottom -= food_.speed
                elif int(abs(nic.rect.bottom - food_.rect.top)) < 40:
                    if food_.direction != nic.direction:
                        food_.direction = nic.direction
                    food_.rect.top += food_.speed
            #"no nicko ,no :<"
            elif food_.size > nic.size:
                if int(abs(food_.rect.bottom - nic.rect.top)) < 40 :
                    if food_.rect.left > nic.rect.left:
                        food_.direction =1
                    elif food_.rect.left <= nic.rect.left:
                        food_.direction =2
                    food_.rect.bottom += food_.speed
                elif int(abs(nic.rect.bottom - food_.rect.top)) < 40:
                    if food_.rect.left > nic.rect.left:
                        food_.direction = 1
                    elif food_.rect.left <= nic.rect.left:
                        food_.direction = 2
                    food_.rect.top -= food_.speed

def main():
    #soul
    pygame.mixer.music.play(-1)
    #like it's an evidence
    nic = nicko.Nicko()
    #agriculture
    init_foods()

    # McDo : open
    running = True
    paused = False


    while running:
        #run nicko, run
        now_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                #McDo : closed
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    paused = not paused
                    
        if not paused:
            #buffer good
            screen.blit(pygame.image.load('images/bf.jpg').convert_alpha(),(0,0))
            #idk how this work but it say how is nicko going
            load_text("Score : %s" % str(nic.score),30,(255,255,255),(10,5))
            #draw pause
            load_icon(unpause_img,(750,10))
            #come nicko
            elude_pursue(nic)
            #foods
            load_foods()
            #boss
            boss_collide(nic)
            #how is nicko going
            nicko_collide(nic)
            #nicko is gonna put some dirt in ur i
            if 100 <= nic.score < 500:
                nic.size = 3
            if 500 <= nic.score:
                nic.size = 5
            nic.bigger()
            
        
            #follow ur heart nicko
            pygame.mouse.set_visible(False)
            nic.rect.center = pygame.mouse.get_pos()

        if paused:
            pygame.mouse.set_visible(True)     
            #draw pause 
            load_icon(pause_img,(750,10))
        else:
            pygame.mouse.set_visible(False)
            new_pos = pygame.mouse.get_pos()
        
            #if nicko is here ,he's here
            if nic.live:
                nic.display_nicko(now_pos,new_pos)
            else:
                pygame.mouse.set_visible(True)     
                #nicko not here, no soul
                pygame.mixer.music.stop()
                die_sound.play()
                paused = True
                load_text("To Be Continued" ,30,(255,0,0),(300,200))
                 
        
        pygame.display.flip()
        #normally 60 fps act 3 but how it work well
        clock.tick(60)
        

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
