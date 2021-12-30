import pygame  

class Map:
    def __init__(self):
       self.x = 12
       self.y = 8
       self.Map = [ 3,3,3,3,3,3,3,3,3,3,3,3,
                    1,3,0,3,0,0,0,0,0,0,0,2,
                    1,0,0,0,0,0,0,0,0,0,0,2,
                    1,0,0,3,0,3,0,0,0,0,0,2,
                    3,3,3,3,3,3,3,3,3,3,3,3,
                    1,0,0,0,0,3,0,0,0,0,0,2,
                    1,0,3,0,0,0,0,0,3,0,0,2,
                    3,3,3,3,3,3,3,3,3,3,3,3]
    
    def creation(self,screen,image_surf):
       bx = 0
       by = 0
       for i in range(0,self.M*self.N):
           if self.maze[ bx + (by*self.M) ] == 1:
               screen.blit(image_surf,( bx * 67 , by * 57))
           bx += 1
           if bx > self.M-1:
               bx = 0 
               by += 1


class Operator() :
    def __init__(self) :
        self.image = pygame.image.load("Image_Op\skd_st.gif")
        
    def attack(self):
        self.image = pygame.image.load("Image_Op\skd_att.gif")
        