#Höfundur: Huginn Þór Jóhannsson
import pygame
from random import randint
pygame.init()
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
WIDTH=800
HEIGHT=640
size=(WIDTH,HEIGHT)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Æfingaverkefni - Pygame")
clock=pygame.time.Clock()
carryOn=True
class Ball():
    def __init__(self,size,fill,speed):
        self.size=size
        self.fill=fill
        self.speed=speed
        self.x=size[2]
        self.y=size[3]
        pygame.draw.ellipse(screen,GREEN,size,fill)
obj=Ball(((WIDTH/2)-125,(HEIGHT/2)-125,250,250),0,10)
while carryOn:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            carryOn=False
    screen.fill(WHITE)
    obj=Ball(((WIDTH/2)-125,(HEIGHT/2)-125,250,250),0,10)
    pygame.display.flip()
    clock.tick(60)
