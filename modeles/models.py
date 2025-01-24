import json
import os
import pandas as pd
import pathlib
from operator import itemgetter
from tabulate import tabulate

parent_directory = pathlib.Path(__file__).parent.resolve()
directory = os.path.expandvars(fr'C:\Users\%username%\Desktop\openclassrooms\P4\data\player')
file_path = os.path.join(directory, 'players.json')




class Player:
    def __init__(self, national_id, name, surname, birthdate):
        self.national_id = national_id
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        
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
                
    