import json
import os
import datetime 

def lecture_json():
    with open("data/bdd.json", 'r') as file:
        data = json.load(file)
    return data


def ecriture_json(data, indent):
    with open("data/bdd.json", 'w') as file:
        json.dump(data, file, indent = indent)