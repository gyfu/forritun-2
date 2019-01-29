import random

listi=["kiddi","Huginn","Elín","Kristrún"]
stodur=["Frummi","Memmi","Stummi","Liði"]
random.shuffle(listi)
def randomStodur():
    lok={}
    n=3
    for x in listi:
        tala=random.randint(0,n)
        lok[x]=stodur[n]
        n-=1
    print(lok)

randomStodur()
