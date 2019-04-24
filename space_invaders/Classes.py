#Höfundur: Huginn Þór Jóhannsson
import pygame
BLACK=(0,0,0)
class Entity():
    def __init__(self,window,pos,size=(50,50)):
        self.window=window
        self.x=pos[0]
        self.y=pos[1]
        self.pos=(self.x,self.y)
        self.size=size
        self.make=self.pos+self.size
        pygame.draw.rect(window,BLACK,pygame.Rect(self.make))
    def move(self):
        press=pygame.key.get_pressed()
        if press[pygame.K_RIGHT]:
            self.x+=1
