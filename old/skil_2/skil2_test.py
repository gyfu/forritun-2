#Höfundur: Huginn Þór Jóhannsson
from skil2_foll import *

def main():
    nafn=input("Hvað heitir þú: ")
    while True:
        val=int(input("Veldu:\n1. Pýþagóras\n2. Margfeldi af\n3. Ferningur\n4. Slétt tala\n5. Flatarmál Hrings\n6. Bank bank\n7. Hætta\n: "))
        if val == 1:
            while True:
                tala1=float(input("Gefðu tölu eitt: "))
                tala2=float(input("Gefðu tölu tvö: "))
                if tala1<=0 or tala2<=0:
                    break
                else:
                    print("{}² + {}² = c²\nc={}".format(tala1, tala2, langhlid(tala1, tala2)))
        elif val == 2:
            while True:
                tala1=int(input("Gefðu tölu eitt(0 til að hætta): "))
                tala2=int(input("Gefðu tölu tvö(0 til að hætta): "))
                if tala1 == 0 or tala2 == 0:
                    break
                else:
                    if margfeldiAf(tala1, tala2):
                        print("{} er margfeldi af {}".format(tala2, tala1))
                    else:
                        print("{} er ekki margfeldi af {}".format(tala2, tala1))
        elif val == 3:
            tala=int(input("Gefðu tölu tenings: "))
            ferningur(tala)
        elif val == 4:
            while True:
                val=input("Gefðu tölu: ")
                try:
                    val = int(val)
                except ValueError:
                    print("Þetta er ekki tala.")
                    continue
                if val == 0:
                    break
                else:
                    if er_slett_tala(val):
                        print("{} er slétt tala".format(val))
                    else:
                        print("{} er odda tala".format(val))
        elif val == 5:
            while True:
                val=input("Gefðu tölu: ")
                try:
                    val=int(val)
                except ValueError:
                    print("Þetta er ekki tala.")
                    continue
                if val == 0:
                    break
                else: 
                    print("Flatarmál hringsins er {}".format(flatarmal_hring(val)))
        elif val == 6:
            tala=input("Gefðu tíma í sekúndum: ")
            try:
                tala=int(tala)
            except ValueError:
                print("Þetta er ekki tala")
                break
            bank_bank(tala)
            print("Hver er þar?")
        elif val == 7:
            print("Bless {}, klukkan er {}".format(nafn, datetime.now().time()))
            break


main()
