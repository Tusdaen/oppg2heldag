import json
import matplotlib.pyplot as plt
import numpy as np
import csv
from pathlib import Path

filnavn = Path(__file__).parent / "sivilstand.json"

with open(filnavn, encoding="utf-8") as fil:
  data = json.load(fil)


filnavnEn = Path(__file__).parent / "Befolkning.csv"

with open(filnavnEn, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")



#Oppg 4 start
filnavn3 = Path(__file__).parent / "Skilsmisser og ekteskap.csv"

x = []
y1 = []
y2 = []
with open(filnavn3, encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")
    
    overskrifter = next(filinnhold)
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