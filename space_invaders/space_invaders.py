#Höfundur: Huginn Þór Jóhannsson
import pygame
import time
from random import randint
from Classes import *
space=pygame.image.load("assets/background-1.png")
pygame.init()
window=pygame.display.set_mode((640,480))
pygame.display.set_caption("Space Invaders!")
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
    pygame.display.flip()        
pygame.quit()
