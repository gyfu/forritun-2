#Höfundur: Huginn Þór Jóhannsson
#Lambda æfingar
#1. Hluti: 3 sniðug lambda föll
samlagning=lambda x,y:x+y
fradrattur=lambda x,y:x-y
margfoldun=lambda x,y:x*y
deiling=lambda x,y:x/y
def reiknivel(x,y):
    return samlagning(x,y),fradrattur(x,y),margfoldun(x,y),deiling(x,y)
def fjorfalda(x):
    return x*4
listi=reiknivel(10,20)
gengur_upp_i_thrist=list((filter(lambda listi:listi%3==0,listi)))
print(listi,"\n",gengur_upp_i_thrist)
print(list(map(fjorfalda,listi)))
