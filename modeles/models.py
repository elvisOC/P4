import json
import os
import pandas as pd
import pathlib
from operator import itemgetter
from tabulate import tabulate
import re
from datetime import datetime
from dataclasses import dataclass, field

@dataclass
class Player:
    identifiant : str
    surname : str
    name : str
    birthdate : str

        
    def __post_init__(self):
        
        if not re.match(r"^[A-Za-z][A-Za-z]\d\d\d\d\d$", self.identifiant):
            raise ValueError("L'identifiant n'est pas au bon format")
        
        if not self.name or not isinstance(self.surname, str):
            raise ValueError("Le prénom doit être une chaine non vide")
        
        if not self.surname or not isinstance(self.name, str):
            raise ValueError("Le nom doit être une chaine non vide")
        
        if not re.match(r"\d\d-\d\d-\d\d\d\d$", self.birthdate):
            raise ValueError("La date de naissance n'est pas au format JJ-MM-AAAA")
        
    def to_dict(self):
        return {
            "ID" : self.identifiant,
            "Name" : self.surname,
            "Surname" : self.name,
            "Birthdate" : self.birthdate
        }
            
        
class Tournoi:
    def __init__(self, nom, lieu, date_debut, date_fin, nb_tours, joueurs, tours):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nb_tours = nb_tours
        self.joueurs = []
        self.tours = []
        
class Tours:
    def __init__(self, numero, start, finish, match):
        self.numero = numero
        self.start = start
        self.finish = finish
        self.match = match
        
class Matchs:
    def __init__(self):
        pass

  
class DAO:
    def charger_file(file_name):
        parent_directory = pathlib.Path(__file__).parent.resolve()
        directory = parent_directory.parent
        file_path = os.path.join(directory, "data", file_name)
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            with open(file_path, 'r', encoding='utf-8') as file:
               return json.load(file)
        return {}

    def sauvegarder_file(file_name, data):
        parent_directory = pathlib.Path(__file__).parent.resolve()
        directory = parent_directory.parent
        file_path = os.path.join(directory, "data", file_name)
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
            
#print(DAO.charger_file('players.json'))