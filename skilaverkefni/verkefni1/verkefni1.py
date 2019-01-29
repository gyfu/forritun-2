#Höfundur: Huginn Þór Jóhannsson
import math, random
#Póstfnúmer: 
def postnumer():
    postnumer={
            "Reykjavík":101,
            "Kópavogur":200,
            "Garðabær":225,
            "Hafnafjörður":220,
            "Reykjanesbær":230,
            "Grindavík":240,
            "Sandgerði":245,
            "Garður":250
            }
    while True:
        val = int(input("Hvað vilt þí gera?\n 1. Leita að póstnúmerum\n 2. Bæta inn nýjum stað og númerum\n 3. Eyða stað úr safni\n 4. Breyta póstnúmeri á stað\n 5. Hætta\n: "))
        if val == 1:
            leit=input("Hvaða póstnúmer viltu fá: ")
            if leit in postnumer:
                print("\nPóstnúmerið skráð á {} er {}\n".format(leit, postnumer[leit]))
            else:
                print("Þessi staður er ekki á skrá.")
        elif val == 2:
            stad=input("Hvað heitir staðurinn: ")
            numer=int(input("Skráðu númerið: "))
            postnumer[stad]=numer
        elif val == 3:
            stad=input("Hvað heitir staðurinn: ")
            if stad in postnumer:
                del postnumer[stad]
            else:
                print("Þessi staður er ekki á skrá.")
        elif val == 4:
            stad=input("Hvað heitir staðurinn: ")
            numer=int(input("Gefu nýtt númer: "))
            postnumer[stad]=numer
        elif val == 5:
            break
        else: 
            return "Veldu tölu frá einum upp í fimm."
