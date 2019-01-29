#Höfundur: Huginn Þór Jóhannsson
from random import *
from math import *
def saeti(numeric):
    if numeric == 1:
        return "Gull"
    elif numeric == 2:
        return "Silfur"
    elif numeric == 3:
        return "Brons"
def kyn(kyn):
    if kyn == "kk":
        return "Þú ert karlmaður"
    elif kyn == "kvk":
        return "Þú ert kvenmaður"
    else:
        fornafn = input("Hvað vilt þú vera kallaður: ")
        fornafn=fornafn.upper()
        return fornafn
def hringur(ummal):#Þú talaðir um í tímanum að nota radíus ekki ummál en í verkefnalýsingu stendur ummál svo ég fór eftir því
    ummal *= ummal
    A = ummal / 4*pi
    return A
def randomTolur():
    templist=[]
    while len(templist) < 81:
        templist.append(randint(0,9))
    return templist
def attaRod(listi):
    tel=0
    for x in listi:
        tel += 1
        if tel != 9:
            print(x,end=" ")
        else:
            tel = 0
            print("\n")
def medaltal(listi):
    x = 0
    for n in listi:
        x+=n
    return x/len(listi)
def searchStr(strengur,leitarord):
    if leitarord in strengur:
        return True
    else:
        return False
