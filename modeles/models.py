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
        
        if not re.match(r"^[A-Z][A-Z]\d\d\d\d\d$", self.identifiant):
            raise ValueError("L'identifiant n'est pas au bon format")
        
        if not self.surname or not isinstance(self.surname, str):
            raise ValueError("Le prénom doit être une chaine non vide")
        
        if not self.name or not isinstance(self.name, str):
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
            
@dataclass
class Tournoi:
    name : str
    location : str
    date_debut : str
    date_fin : str
    nb_tours : int 
    description : str
    current_round : int = 0
    
    def __post_init__(self):
        
        if not self.name or not isinstance(self.name, str):
            raise ValueError("Le nom doit être une chaine non vide")
        if not self.location or not isinstance(self.location, str):
            raise ValueError("Le lieu doit être une chaine non vide")
        if not re.match(r"\d\d-\d\d-\d\d\d\d$", self.date_debut):
            raise ValueError("La date de début n'est pas au bon format JJ-MM-AAAA")
        if not re.match(r"\d\d-\d\d-\d\d\d\d$", self.date_fin):
            raise ValueError("La date de fin n'est pas au bon format JJ-MM-AAAA")
        if self.nb_tours is None:
            self.nb_tours = 4
        if not isinstance(self.nb_tours, int):
            raise ValueError("Le nombres de tours doit être en chiffre")
        if not self.description or not isinstance(self.description, str):
            raise ValueError("La description doit être une chaine non vide")
        
        
    def to_dict(self):
        return {
            "name" : self.name,
            "location" : self.location,
            "start_date" : self.date_debut,
            "end_date" : self.date_fin,
            "number_of_rounds" : self.nb_tours,
            "current_round" : self.current_round,
            "description" : self.description
        }
        
        
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