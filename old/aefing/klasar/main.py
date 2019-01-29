#Höfundur: Huginn Þór Jóhannsson
tvær mótlægar hliðar eru samsíða.from math import *
class Trapisa():
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.s=(a+b+c+d)/2
    def ummal(self):
        return self.a+self.b+self.c+self.d
    def flatarmal(self):
        lidur1=(self.a+self.c)/(self.a-self.c)
        lidur2=sqrt((self.s -self.c)*(self.s -self.a)*(self.s-self.c-self.b)*(self.s-self.c-self.d))
        svar=lidur2*lidur1
        if svar < 0:
            return svar*(-1)
        else:
            return svar
    def flatarmalHaed(self):
        pass
    def jafnarma(self):
        if c == d:
            return True
        else:
            return False
    def lestuMig(self):
        return "Trapisa eða hálfsamsíðungur er ferhyrningur þar sem tvær mótlægar hliðar eru samsíða."
class Bill():
    def __init__(self,tegund,argerd,hradi,bensin,eydsla):
        self.tegund=tegund
        self.argerd=argerd
        self.hradi=hradi
        self.bensin=bensin
        self.eydsla=eydsla

