#Höfundur: Huginn Þór Jóhannsson
from math import *
from time import *
from datetime import *
def langhlid(a,b):
    a*=a
    b*=b
    c=a+b
    return sqrt(c)
def margfeldiAf(a,b):
    if b%a==0:
        return True
    else: 
        return False
def ferningur(x):
    for n in range(x):
        print("*"*x)
def er_slett_tala(x):
    if x%2==0:
        return True
    else:
        return False
def flatarmal_hring(r):
    a=pi*(r*r)
    return a
def bank_bank(s):
    end=time()+s
    while time() < end:
        print("bank")
        sleep(0.2)
