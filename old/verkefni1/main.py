#Höfundur: Huginn Þór Jóhannsson
from random import *
def mkPhone():
    phonebook = {
            "Jónas":0,
            "Haraldur":1,
            "Kamila":2,
            "Konni":3,
            "Jóna":4,
            "Palli":5,
            "Arnar":6,
            "Elvar":7,
            "Anna":8,
            "Kristín":9,
            }
    for x in phonebook:
        phonebook[x]=randint(1000000, 9999999)
    return phonebook
def srchPhone(phonebook, leitarord):    return phonebook.get(leitarord,"Þetta nafn er ekki á skrá")
def addNum(phonebook,name,number):
    phonebook[name]=number
    return phonebook
def rmNum(phonebook,name):
    if name in phonebook:
        del phonebook[name]
        return phonebook
    else:
        print("Þetta nafn er ekki á skrá")
        return phonebook
def chngNum(phonebook,name, newnum):
    if name in phonebook:
        phonebook[name]=newnum
        return phonebook
    else:
        print("Þetta nafn er ekki á skrá")
        return phonebook
def lidur1():
    simaskra=mkPhone()
    while True:
        print(simaskra)
        valmynd=input("Valmynd:\n1. Leita í síma\n2. Bæta við númeri\n3. Eyða númeri\n4. Breyta númeri\n5. Hætta\n: ")
        if valmynd=="1":
            val=input("Hverjum viltu leita að: ")
            print("\nSímanúmerð fyrir {} er {}\n".format(val,srchPhone(simaskra,val)))
        elif valmynd=="2": 
            nafn=input("Nafn: ")
            numer=int(input("Númer: "))
            simaskra=chngNum(simaskra,nafn,numer)
        elif valmynd=="3":
            val=input("Númer hvers viltu eyða: ")
            simaskra=rmNum(simaskra,val)
        elif valmynd=="4":
            val=input("Númer hvers viltu breyta: ")
            num=int(input("Nýtt númer: "))
            simaskra=chngNum(simaskra,val,num)
        elif valmynd=="5":
            break
        else:
            print("\nVeldu tölu frá einum upp í fimm.\n")
#lidur1()
#Liður tvö:-----------------------------------------------------------
def mkList():
    numeric=int(input("Hve margir eru skráðir í hópinn: "))
    templist=[]
    for x in range(numeric):
        templist.append(input("Gefðu nafn einstaklings í hópinum: "))
    templist.sort()
    return templist
FOR=mkList()
GSO=mkList()
def compareList(list1, list2):
    templist=[]
    for x in list1:
        if x in list2:
            templist.append(x)
    return templist
def listSize(list1, list2):
    if len(list1) > len(list2):
        return True
    else:
        return False
def faeraNemendur():
    
