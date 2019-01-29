#Höfundur: Huginn Þór Jóhannsson
import math, random
#Sæti: 

#Kyn: 

#Flatarmál út frá radíus: 

#80random: 

#Meðaltal: 

#Main: 
def main():
    def valmynd():
        switch["einn","tveir","þrír","fjórir","fimm"]
    while True:
        val=int(input("Veldu tölu frá einum upp í sex: "))
        if val in range(1, 5):
            switch[val]
        elif val == 6:
                break
        else: 
            print("Veldu tölustaf á bilinu 1-6\n")
main()
