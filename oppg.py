import csv
filnavnEn = "Befolkning.csv"

with open(filnavnEn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")
    
print("hei")