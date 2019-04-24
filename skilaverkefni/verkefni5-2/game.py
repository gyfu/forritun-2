#Höfundur: Huginn Þór Jóhannsson
from random import randint
from tening import Tening
from takki import Takki
import time
import pygame
GREEN=(0,150,0)
pygame.init()
window=pygame.display.set_mode((800,640))
window.fill(GREEN)
pygame.display.set_caption("Teningar")
running=True
clock=pygame.time.Clock()
clock_ticks=20
posx=30
def teningar(posx):
    listi=[]
    tel=0
    for x in range(6):
        posx+=70
        tel+=1
        listi.append(Tening(window,tel,posx,100))
    return listi
listi=teningar(posx)
while running:
    takki1=pygame.Rect(100,200,100,200)
    takki2=pygame.Rect(210,410,100,200)
    score=pygame.Rect(500,500,200,200)
    for event in pygame.event.get():
        if event.type==pygame.QUIT or event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
            running=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                for x in listi:
                    if x.button.collidepoint(event.pos):
                        x.clicked=1
                #for x in listi:
                #    if x.clicked==0:
                #        x.breytaVal(randint(1,6))
                
    pygame.display.update()
    clock.tick(clock_ticks)
pygame.quit()
