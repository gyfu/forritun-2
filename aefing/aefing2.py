#Höfundur: Huginn Þór Jóhannsson
def alphabet():
    temp = {"a":"afi","b":"borð","c":"cookie","d":"draugur","e":"epli","f":"fótur","g":"gestur","h":"hurð","i":"innirödd","j":"jól","k":"kamar","l":"ljós","m":"maður","n":"noregur","o":"ofn"}
    return temp

def printAlphabet(alphabet):
    for x in alphabet:
        print ("{} fyrir {}.".format(x, alphabet[x]))

def returnE(alphabet):
    return alphabet["e"] 

def breytaH(alphabet):
    for x in alphabet:
        if x == "h":
            alphabet[x] = "hestur"
    return alphabet
def rmC(alphabet):
    temp = dict(alphabet)
    del temp["c"]
    return temp
print(rmC(alphabet()))
