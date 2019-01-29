#Höfundur: Huginn Þór Jóhannsson
import random
teststring = "bla Sabla blsíða"
def wordCount(string):
    utkoma = string.split()
    return len(utkoma)
def fyrstuFimm(string):
    return string[0:5]
def sidustuFjorir(string):
    return string[-4:]
def middle(string):
    lengd = len(string)
    if lengd%2:
        return string[lengd//2]
    else:
        texti = "Þessi texti hefur enga miðju, slétt tala"
        return texti
def finnaS(string):
    nyr = ""
    for x in string:
        if x == "s" or x == "S" or x == " ":
            nyr += x
        else:
            nyr += "$"
    return nyr
def randomList100():
    listi = []
    for x in range(100):
        listi.append(random.randint(34, 68))
    return listi
def listiSorted(listi):
    return sorted(listi)
def medaltal(listi):
    tala = 0
    for x in listi:
        tala += x
    return tala / len(listi)
def minMax(listi):
    mini = min(listi)
    maxi = max(listi)
    strengur = "Stærsta talan í listanum er {} og minnsta er {}".format(mini, maxi)
    return strengur
def shrink(listi):
    while sum(listi) > 4500:
        listi.pop(-1)
def fiveReduce(listi):
    newlist = []
    for x in listi:
        if x % 5 != 0:
            newlist.append(x)
    return newlist
def list40(listi):
    newlist = []
    for x in listi:
        if x == 40:
            newlist.append(x)
    return newlist
print(list40(randomList100()))
