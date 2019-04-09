#Höfundur: Huginn Þór Jóhannsson
from random import randint
import pygame
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
WHITE=(255,255,255)
BLACK=(0,0,0)
class Tening:
    def __init__(self,pos,value):
        self.pos=pos
        self.value=value
        self.size=(60,60)
        self.args=(value[0],value[1],self.size[0],self.size[1])
        self.color=RED
th_init=[randint(1,6) for i in range(6)]
def counter():
    seen={}
    dupes=[]
    for x in th_init:
        if x not in seen:
            seen[x] = 1
        else: 
            if x not in dupes:
                dupes.append(x)
            seen[x]+=1
    return seen
def score(count):
    score=0
    if len(count)==6:
        score+=500
    else:
        bonus=0
        for x, y in count.items():
            if y == 2:
                score+=20
                bonus+=1
                if bonus==3:
                    score+=40
            elif y == 3:
                score+=80
            elif y==4:
                score+=250
            elif y==5:
                score+=350
            elif y==6:
                score+=600
    return score
