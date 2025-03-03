from database import *
from config import *
from datetime import datetime


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
    montant_a_payer = 0
    for voiture in voitures:
        if voiture["plaque"] == plaque:
            heure_entree = datetime.strptime(voiture["entree"], "%H:%M:%S")
            heure_entree = int(heure_entree)
            heure_sortie = datetime.now()
            duree = heure_sortie - heure_entree
            heures = duree.total_seconds() / 3600
            montant_a_payer = heures * tarif
            print(f"Montant à payer: {montant_a_payer:.2f} euros")
        else:
            nouvelles_voitures.append(voiture)
    data["voitures"] = nouvelles_voitures

    ecriture_json(data, 4)