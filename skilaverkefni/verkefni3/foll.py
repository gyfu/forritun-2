#Höfundur: Huginn Þór Jóhannsson
import csv
def opnaSkra(skra):
    with open(skra,"r") as f:
        lines=csv.reader(f)
    return lines
print(opnaSkra("veralydsfelag.csv"))
