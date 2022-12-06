import json

filnavn = "sivilstand.json"

with open(filnavn, encoding="utf-8") as fil:
  data = json.load(fil)

print(data)