#Höfundur: Huginn Þór Jóhannsson
import pygame
from random import randint
def dots(value,posx,posy,window):
    dot=lambda x:pygame.draw.circle(window,(255,255,255),x,7)
    center=(posx+30,posy+30)
    midr=(posx+50,posy+30)
    midl=(posx+10,posy+30)
    topl=(posx+10,posy+10)
    topr=(posx+50,posy+10)
    bottoml=(posx+10,posy+50)
    bottomr=(posx+50,posy+50)
    if value==1:
        dot(center)
    elif value==2:
        dot(topl),dot(bottomr)
    elif value==3:
        dot(topl),dot(bottomr),dot(center)
    elif value==4:
        dot(topl),dot(topr),dot(bottoml),dot(bottomr)
    elif value==5:
        dot(topl),dot(topr),dot(bottoml),dot(bottomr),dot(center)
    elif value==6:
        dot(midl),dot(midr),dot(topl),dot(topr),dot(bottoml),dot(bottomr)
class Tening:
    def __init__(self,window,value,posx,posy,sizex=60,sizey=60):
        self.value=value
        self.posx=posx
        self.posy=posy
        self.make=(posx,posy,sizex,sizey)
        self.window=window
        self.RED=(255,0,0)
        self.WHITE=(255,255,255)
        self.button=pygame.Rect(self.make)
        pygame.draw.rect(window,self.RED,self.button)
        dots(value,posx,posy,window)
        self.clicked=0
    def breytaVal(self,val):
        self.value=val
        pygame.draw.rect(self.window,self.RED,self.button)
        dots(self.value,self.posx,self.posy,self.window)
    def cl(self):
        if self.button.collidepoint(event.pos):
            self.clicked=1
        else:
            self.clicked=0

