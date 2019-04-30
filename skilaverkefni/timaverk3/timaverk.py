#Höfundur: Huginn Þór Jóhannsson
from random import randint
#Liður Eitt
def reverse():
    x=str(input("insert num: "))
    y=str(input("insert num: "))
    x=int(str(x)[::-1])
    y=int(str(y)[::-1])
    print("{} + {} = {}".format(x,y,x+y))
#Liður Tvö
class Timaverk3():
    def __init__(self,kyn,aldur):
        if kyn=="kvk":
            self.kyn="Kona"
        elif kyn=="kk":
            self.kyn="Karlmaður"
        else:
            self.kyn="af Óræðu kyni"
        if aldur>=20:
            self.aldur="Fullorðin"
        elif aldur>=13:
            self.aldur="Unglingur"
        elif aldur>= 0 and aldur <=12:
            self.aldur="Barn"
    def upplysingar(self):
        strengur="Þú ert {} og ert {}.".format(self.kyn,self.aldur)
        return strengur
    def milli(self):
        a=int(input("Sláðu inn tölu: "))
        b=int(input("Sláðu inn tölu: "))
        c=int(input("Sláðu inn tölu: "))
        listi=[a,b,c]
        range_max=max(listi)
        range_min=min(listi)
        new_list=[]
        for x in range(range_min,range_max):
            if x in listi:
                pass
            else:
                new_list.append(x)
        print(new_list)
    def konni(self):
        listi=[]
        while True:
            tala=int(input("Sláðu inn nokkrar tölur(0 til að hætta): "))
            if tala==0:
                break
            else:
                listi.append(tala)
        new_list=[]
        for x in listi:
            if x > 40 and str(x).endswith("1"):
                new_list.append(x)
        print(new_list)
def object_generator():
    listi=[]
    kyn=["kvk","kk","else"]
    for x in range(20):
        sex=randint(0,2)
        age=randint(0,100)
        listi.append(Timaverk3(kyn[sex],age))
    return listi
#Liður Þrjú
class Frum():
    def __init__(self,nafn):
        self.nafn=nafn
    def upplysingar(self):
        return("Halló ég er klassinn Frum og heiti {}.".format(self.nafn))
class Fyrsti(Frum):
    def __init__(self,nafn,setning,tala):
        Frum.__init__(self,nafn)
        self.setning=setning
        self.tala=tala
        self.listi=[setning for x in range(tala)]
    def setningarlisti(self):
        return(self.listi)
def main():
    while True:
        val=input("Hvað viltu prufa?\n 1. Liður\n 2. Liður\n 3. Liður\n 4. Hætta\n: ")
        try:
            val=int(val)
        except:
            print("Veldu tölu frá 1 - 4")
        if val == 1:
            reverse()
        elif val == 2:
            annad_val=input("Hvað viltu prufa í öðrum lið?\n 1. Fallið Upplýsingar\n 2. Fallið Milli\n 3. Fallið Konni\n 4. Hætta\n: ")
            try:
                annad_val=int(annad_val)
            except:
                print("Veldu tölu frá 1 - 4")
            if annad_val==1:
                listi=object_generator()
                for x in listi:
                    print(x.upplysingar())
            elif annad_val==2:
                obj1=Timaverk3("kvk",0)
                obj1.milli()
            elif annad_val==3:
                obj1=Timaverk3("kvk",0)
                obj1.konni()
            elif annad_val==4:
                break
        elif val == 3:
            obj1=Frum(input("Veldu nafn: "))
            print(obj1.nafn)
            print(obj1.upplysingar())
            obj2=Fyrsti(input("Veldu nafn: "),input("Veldu setningu: "),int(input("Hversu oft viltu að setningin birtist: ")))
            print(obj2.nafn)
            print(obj2.upplysingar())
            print(obj2.setningarlisti())
        elif val == 4:
            break
main()





