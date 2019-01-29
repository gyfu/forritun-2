#Höfundur: Huginn Þór Jóhannsson
from random import *
from math import *
from time import *
from datetime import *

def giskaTolu():
    def gisk(gisk,tala):
        if gisk == tala:
            return True
        elif gisk < tala:
            print("Tala of lág, reyndu aftur")
        elif gisk > tala:
            print("tala of há, reyndu aftur")
    tala=randint(1,1000)
    while True:
        val=input("Veldu tölu frá 1-1000:\n ")
        try: val=int(val)
        except ValueError: 
            print("Einungis tölustafi.")
            continue
        if gisk(val,tala):
            print("Þú ert sigurvegari!")
        if val == 0:
            break
def pening():
    def kastaPening():
        if randint(0,1)==1:
            return True
        else:
            return False
    heads=0
    tails=0
    while True:
        val=input("Veldu\n 1. Kasta pening\n 2. Hætta\n: ")
        try:
            val=int(val)
        except ValueError:
            print("Veldu einungis 1 eða 2")
        if val == 1:
            if kastaPening():
                heads+=1
            else:
                tails+=1
        elif val == 2:
            break
        else:
            print("Veldu einungis 1 eða 2")
        print("Lúða = {}\nSkjaldamerki = {}".format(heads,tails))
def takk():
    n=1.0
    while True:
        sleep(n)
        print("takk")
        n-=0.1
        if n < 0.1:
            print("Eigðu góðan dag.")
            break
    now=datetime.now()
    print(now.strftime("%Y-%m-%d %A"))
def valmynd():
    val=input("Veldu\n 1. Gisk leik\n 2. Peningakast\n 3. Takk\n 4. Hætta\n: ")
    try: val=int(val)
    except ValueError:
        print("Verður að vera tala")
    if val in [1,2,3,4]:
        return val
    else:
        print("Verður að vera tala frá 1-4")
def main():
    while True:
        val = valmynd()
        if val == 1:
            giskaTolu()
        elif val == 2:
            pening()
        elif val == 3:
            takk()
        elif val == 4:
            break
main()
