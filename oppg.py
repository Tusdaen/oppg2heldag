import csv
import json
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

filnavn = Path(__file__).parent / "Siviltilstand.json"

with open(filnavn, encoding="utf-8") as fil:
    data = json.load(fil)

aarstallListe = []
for aarstall in data["dataset"]["dimension"]["Tid"]["category"]["index"]:
    aarstallListe.append(int(aarstall))
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
#plt.legend()
plt.xlim(aarstallListe[1],aarstallListe[-1])
#plt.show()


filnavn2 = Path(__file__).parent / "Befolkning.csv"

aarstall = []
befolkning = []

with open(filnavn2, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")
    
    overskrifter = next(filinnhold)
    tomrad = next(filinnhold)
    akseoverskrift = next(filinnhold)
    print(overskrifter)

    for rad in filinnhold:
      aarstall.append(int(rad[0]))
      befolkning.append(int(rad[1]))

plt.plot(aarstall, befolkning, label="Befolkning")
plt.title("Befolkningsvekst og silviltilstand fra 1769 til 2022")
plt.legend()
plt.ylim(0)
plt.show()



#Oppg 4 start
filnavn3 = Path(__file__).parent / "Skilsmisser og ekteskap.csv"

x = []
y1 = []
y2 = []
with open(filnavn3, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")
    
    overskrifter3 = next(filinnhold)
    ignorer = next(filinnhold)
    print(overskrifter)

    teller = 0
    for rad in filinnhold:
      if teller == 0:
        x = rad
      if teller == 1:
        y1 = rad
      if teller == 2:
        y2 = rad
      teller += 1

labelx = x[0]
labely1 = y1[0]
labely2 = y2[0]
x.pop(0)
y1.pop(0)
y2.pop(0)

for i in range(len(y1)):
  if y1[i] == "..":
    y1[i] = "0"
for i in range(len(y2)):
  if y2[i] == "..":
    y2[i] = "0"

y1 = [int(x) for x in y1]
y2 = [int(x) for x in y2]

fig, ax = plt.subplots(figsize=(10,10))

y = np.arange(13)

ax.bar(y+0.2, y1, width=0.4, label=labely1)
ax.bar(y-0.2, y2,width=0.4, label=labely2)
ax.set_xticks(y,x)
ax.legend()

plt.show()