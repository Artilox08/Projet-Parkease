from parking import *
from database import *
from config import *
from datetime import datetime

data = lecture_json()
place_dispo = len(data.get("voitures"))

plaque = str(input("Veuillez entrer votre plaque d'immatriculation: "))

voitures = data.get("voitures", [])
plaque_existe = any(voiture.get("plaque") == plaque for voiture in voitures)

heure = datetime.now()
heure = heure.strftime("%H:%M:%S")

if plaque_existe == False:
    if place_dispo < place_total:
        enter(plaque,heure)
        print("Bienvenue!")
    elif place_dispo >= place_total:
        print("Plus de place disponible")

elif plaque_existe == True:
    exit(plaque)
    print("Au revoir!")