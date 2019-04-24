#Höfundur: Huginn Þór Jóhannsson
import pygame
import time
from random import randint
from Classes import Entity
space=pygame.image.load("assets/background-1.png")
pygame.init()
window=pygame.display.set_mode((640,480))
window.fill((255,255,255))
def main():
    running=True
    window.fill((255,255,255))
    window.blit(space,(0,0))
    ob1=Entity(window,(0,0))
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT or event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                running=False
        ob1.move()
        pygame.display.flip()
main()
pygame.quit()
