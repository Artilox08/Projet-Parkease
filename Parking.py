import json
from database import *


def enter(plaque, heure):
    data = lecture_json()
    
    nouvelle_voiture = {
        "plaque": plaque,
        "entree": heure
    }
    data["voitures"].append(nouvelle_voiture)
    
    ecriture_json(data,4)





def exit(plaque):
    data = lecture_json()

    voitures = data["voitures"]
    nouvelles_voitures = []
    for voiture in voitures:
        if voiture["plaque"] != plaque:
            nouvelles_voitures.append(voiture)
    data["voitures"] = nouvelles_voitures

    ecriture_json(data,4)