#Höfundur: Huginn Þór Jóhannsson
import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self,window,x,y,w=64,h=64):
        pygame.sprite.Sprite.__init__(self)
        self.window=window
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.vel=5
    def draw(self):
        pygame.draw.rect(self.window,(255,0,0),(self.x,self.y,self.w,self.h))
class Missile(Entity):
    def __init__(self,window,x,y):
        Entity.__init__(self,window,x,y,w=10,h=10)
        self.vel=10
    def move(self):
        self.y-=self.vel
class Player(Entity):
    def __init__(self,window,x,y):
        Entity.__init__(self,window,x,y)
        self.missiles=[]
    def shoot(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            new_missile=Missile(self.window,self.x+22,self.y)
            self.missiles.append(new_missile)
    def move(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.x > self.vel:
                self.x-=self.vel
        if keys[pygame.K_RIGHT]:
            if self.x < 640 - self.vel - 64 - 5:
                self.x+=self.vel

class Invader(Entity):
    def __init__(self,window,x,y):
        Entity.__init__(self,window,x,y)
        self.direction=0
        self.alive=0
    def move(self):
        if self.direction==0:
            if self.x > self.vel:
                self.x-=self.vel
            else:
                self.direction=1
        if self.direction==1:
            if self.x < 640 - self.vel - 64:
                self.x+=self.vel
            else:
                self.direction=0
    def shot(self,posx,posy):
        pass
