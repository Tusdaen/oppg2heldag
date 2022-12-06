#import json

#filnavn = "sivilstand.json"

#with open(filnavn, encoding="utf-8") as fil:
#  data = json.load(fil)

#print(data)

import csv
import matplotlib.pyplot as plt
filnavnEn = "Befolkning.csv"

aarstall = []
befolkning = []

with open(filnavnEn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")

    overskrifter = next(filinnhold)
    print(overskrifter)

    for rad in filinnhold:
      aarstall.append(rad[0])
      befolkning.append(rad[1])

plt.plot(aarstall, befolkning)
plt.title("Befolkningsvekst fra 1769 til 2022")
plt.show



