class felag():
    def __init__(self,numer,nafn,laun,kennitala):
        self.numer=numer
        self.nafn=nafn
        self.laun=laun
        self.kennitala=kennitala
    def skatt(self):
        return int(self.laun)*0.36
    def utborgun(self):
        mon=int(self.laun)
        return mon - mon*0.36
    def info(self):
        return "Félagsnúmer: {}\nNafn félaga: {}\nLaun félaga: {}\nKennitala félaga: {}".format(self.numer,self.nafn,self.laun,self.kennitala)
