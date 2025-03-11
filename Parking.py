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
            heure_entree = datetime.strptime(voiture["entree"], "%H:%M")
            heure_entree_seconds = heure_entree.hour * 3600 + heure_entree.minute * 60 + heure_entree.second
            heure_sortie = datetime.now()
            heure_sortie_seconds = heure_sortie.hour * 3600 + heure_sortie.minute * 60 + heure_sortie.second
            duree_seconds = heure_sortie_seconds - heure_entree_seconds
            if duree_seconds < 0:
                duree_seconds += 24 * 3600  # Ajustement pour les passages de jour
            heures = (duree_seconds + 3599) // 3600  # Arrondir à l'entier supérieur
            montant_a_payer = heures * tarif
            print(f"Montant à payer: {montant_a_payer:.2f} euros")
        else:
            nouvelles_voitures.append(voiture)
    data["voitures"] = nouvelles_voitures

    ecriture_json(data, 4)