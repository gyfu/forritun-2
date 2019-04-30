#Höfundur: Huginn Þór Jóhannsson
import pygame
import time
from random import randint
from Classes import Entity, Player, Invader
space=pygame.image.load("assets/background-1.png")
pygame.init()
window=pygame.display.set_mode((640,480))
pygame.display.set_caption("Space Invaders!")
x=10
y=420
running=True
jumping=False
airTime=10
while running:
    pygame.time.delay(100)
    window.fill((255,255,255))
    window.blit(space,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT or event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
            running=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>10:
        x-=10
    if keys[pygame.K_RIGHT] and x<580:
        x+=10
    if not(jumping):
        if keys[pygame.K_UP] and y>10:
            y-=10
        if keys[pygame.K_DOWN] and y<420:
            y+=10
        if keys[pygame.K_SPACE]:
            jumping=True
    else:
        if airTime > -10:
            neg=1
            if airTime < 0:
                neg=-1
            y-=(airTime **2) *0.5*neg
            airTime-=1
        else:
            jumping=False
            airTime=10
    player=Player(window,(x,y))
        
    pygame.display.flip()        
pygame.quit()
