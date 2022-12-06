import json
import matplotlib.pyplot as plt

filnavn = "Siviltilstand.json"

with open(filnavn, encoding="utf-8") as fil:
    data = json.load(fil)

aarstallListe = []
for aarstall in data["dataset"]["dimension"]["Tid"]["category"]["index"]:
    aarstallListe.append((aarstall))
#print(aarstallListe)

ugift = []
gift = []
enke = []
separert = []
skilt = []

for i in range(42):
    ugift.append(data["dataset"]["value"][i])

for i in range(42,84):
    gift.append(data["dataset"]["value"][i])

for i in range(84,126):
    enke.append(data["dataset"]["value"][i])

for i in range(126,168):
    separert.append(data["dataset"]["value"][i])

for i in range(168,210):
    skilt.append(data["dataset"]["value"][i])

plt.plot(aarstallListe, ugift, label="Ugift")
plt.plot(aarstallListe, gift, label="Gift")
plt.plot(aarstallListe, enke, label="Enke/enkemann")
plt.plot(aarstallListe, separert, label="Separert")
plt.plot(aarstallListe, skilt, label="Skilt")
plt.xticks(rotation=45)
plt.legend()
plt.show()

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
plt.show()



