import csv
def opnaSkra(x,mode):
    if mode:
        with open(x,"r") as f:
           reader=csv.DictReader(f)
           return reader[0]

print(opnaSkra("lagerhlutir.csv",1))
