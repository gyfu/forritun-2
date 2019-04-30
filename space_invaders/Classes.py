#Höfundur: Huginn Þór Jóhannsson
import pygame
BLACK=(0,0,0)
class Entity():
    def __init__(self,window,pos):
        self.window=window
        self.pos=pos
        self.size=(50,50)
        self.make=self.pos+self.size
class Player(Entity):
    def __init__(self,window,pos):
        Entity.__init__(self,window,pos)
        pygame.draw.rect(self.window,BLACK,pygame.Rect(self.make))
class Invader(Entity):
    def __init__(self,window,pos,var=0):
        Entity.__init__(self,window,pos)
        self.var=var
        if var==0:
            pygame.draw.rect(self.window,BLACK,pygame.Rect(self.make))
