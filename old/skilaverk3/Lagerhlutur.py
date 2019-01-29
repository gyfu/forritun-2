#Höfundur: Huginn Þór Jóhannsson
from foll import *
class Lagerhlutur():
    def __init__(self,numer,tegund,fjoldi,verd):
        self.numer=numer
        self.tegund=tegund
        self.fjoldi=fjoldi
        self.verd=verd
    def return_all(self):
        return (self.numer,self.tegund,self.fjoldi,self.verd)
    def heildarverd(self):
        return self.verd*self.fjold


