#Höfundur: Huginn Þór Jóhannsson
#1. Hluti: Erfðir
class Automobile():
    def __init__(self, verd, litur):
        self.verd=verd
        self.litur=litur
    def info(self):
        return self.verd, self.litur

class Bike(Automobile):
    def __init__(self,verd,litur,tegund,name,wheels,gears):
        Automobile.__init__(self,verd,litur)
        self.tegund=tegund
        self.name=name
        self.wheels=wheels
        self.gears=gears
    def bikeInfo(self):
        return self.verd,self.litur,self.tegund,self.name,self.wheels,self.gears

class Car(Automobile):
    def __init__(self,verd,litur,speedX,wheels):
        Automobile.__init__(self,verd,litur)
        self.speedX=speedX
        self.wheels=wheels
    def carInfo(self):
        return self.verd,self.litur,self.speedX,self.wheels

class Plow(Automobile):
    def __init__(self,verd,litur, plowSize, tracks):
        Automobile.__init__(self,verd,litur)
        self.plowSize=plowSize
        self.tracks=tracks
    def plowInfo(self):
        return self.verd,self.litur,self.plowSize,self.tracks

ob1=Bike(30000,"green","test","name",2,6)
print(ob1.info())
