#Höfundur: Huginn Þór Jóhannsson
import random, math
#Póstnúmer: 
def postnumer():
    postnumer={
            "Reykjavík":[101,102,103,104,105,107,108,109,110,111,112,113,116],
            "Seltjarnarnes":[170],
            "Kópavogur":[200,201,202,203],
            "Garðabær":[210,212],
            "Hafnafjörður":[220,221,222]
            }
    def edit():
        place = input("Hvaða stað viltu breyta póstnúmeri hjá: ")
        if place in postnumer:
            numer=[]
            while True:
                add=int(input("Hvaða póstnúmer viltu bæta við(0 til að hætta): "))
                if add == 0:
                    break
                else:
                    numer.append(add)
            return postnumer[place]+numer
        else: 
            return 0
    def search():
        place=input("Hvaða póstnúmer viltu finna: ")
        return postnumer[place]
    def add():
        place=input("Hvað heitir staðurinn: ")
        if place in postnumer:
            return "Þessi staður er nú þegar á skrá."
        else:
            numer=[]
            while True:
                add=int(input("Hvaða póstnúmer viltu bæta við(0 til að hætta): "))
                if add.len() != 3:
                    print("Póst númer verður að vera þrír tölustafir")
                else:
                    numer.append(add)
        postnumer[place]=numer
    while True:
        val=int(input("Hvað viltu gera: "))
        if val == 1:
            print(search())
        elif val == 2:
            add()
        elif val == 3: 
            delete()
        elif val == 4: 
            edit()
        elif val == 5:
            break
        else: 
            print("Veldu tölustaf frá 1 - 5.")
postnumer()
