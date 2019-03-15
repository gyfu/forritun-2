#Höfundur: Huginn Þór Jóhannsson
class trapisaTest():
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    def ummal(self):    return self.a+self.b+self.c+self.d
ob1=trapisaTest(10,10,10,10)
print(ob1.ummal())
