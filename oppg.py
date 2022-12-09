import csv
import json
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Oppgave 2

# Importerer json-filen
filnavn = Path(__file__).parent / "Siviltilstand.json"

with open(filnavn, encoding="utf-8") as fil:
    data = json.load(fil)

# Legger årstall-verdiene i en liste
aarstallListe = []
for aarstall in data["dataset"]["dimension"]["Tid"]["category"]["index"]:
    aarstallListe.append(int(aarstall))

# Lager liste til hver sivilstand og legger til verdiene fra filen 
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

# plotter de ulike grafene
plt.plot(aarstallListe, ugift, label="Ugift")
plt.plot(aarstallListe, gift, label="Gift")
plt.plot(aarstallListe, enke, label="Enke/enkemann")
plt.plot(aarstallListe, separert, label="Separert")
plt.plot(aarstallListe, skilt, label="Skilt")
# roterer x-akse-verdiene
plt.xticks(rotation=45)
# Bestemmer hvilken x-verdier som skal vises i grafen fra årstall
plt.xlim(aarstallListe[1],aarstallListe[-1])

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
plt.title("Befolkningsvekst og sivilstand fra 1769 til 2022")
plt.legend()
plt.ylim(0)
plt.show()

#Oppg 4 start
filnavn3 = Path(__file__).parent / "Skilsmisser og ekteskap.csv"

#Her definerer jeg listene som skal brukes senere
x = []
y1 = []
y2 = []

#Denne delen leser grafen og legge verdiene inn i lister
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

#Her tar jeg ut de første verdiene av hver liste fordi de ikke er verdier, men labels
labelx = x[0]
labely1 = y1[0]
labely2 = y2[0]
x.pop(0)
y1.pop(0)
y2.pop(0)

#Her gjør jeg om alle verdier som er ".." til 0. Programmet hadde blitt forvirret om jeg prøvde å inte ".." og jeg kan gjøre verdiene om til 0 fordi det er et bar diagram. Det betyr at 0 verdier bare ikke viser noe. Om det var en vanlig graf hadde en 0 verdi her ødelagt grafen.
for i in range(len(y1)):
  if y1[i] == "..":
    y1[i] = "0"
for i in range(len(y2)):
  if y2[i] == "..":
    y2[i] = "0"

#Her gjør jeg alle verdiene i listen til int
y1 = [int(x) for x in y1]
y2 = [int(x) for x in y2]

#Dette lager og viser grafen
fig, ax = plt.subplots(figsize=(7,7))

y = np.arange(13)

ax.bar(y+0.2, y1, width=0.4, label=labely1)
ax.bar(y-0.2, y2,width=0.4, label=labely2)
ax.set_xticks(y,x)
plt.title("Skilsmisse og ekteskap")
ax.legend()

plt.show()