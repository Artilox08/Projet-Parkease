from parking import *
from database import *
from config import *

data = lecture_json()
place_dispo = len(data.get("voitures"))

plaque = input("Veuillez entrer votre plaque d'immatriculation: ")

voitures = data.get("voitures", [])
plaque_existe = any(voiture.get("plaque") == plaque for voiture in voitures)

# if plaque_existe != True: