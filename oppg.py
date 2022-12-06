import json

filnavn = "sivilstand.json"

with open(filnavn, encoding="utf-8") as fil:
  data = json.load(fil)

print(data)

import csv
filnavnEn = "Befolkning.csv"

with open(filnavnEn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")
    