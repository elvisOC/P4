from modeles.models import Player, Tournoi, DAO
from vue.view import View
import os
import pathlib
from operator import itemgetter
from tabulate import tabulate
import pandas
import json

actual_directory = pathlib.Path(__file__).parent.resolve()
directory = actual_directory.parent
#player_path = os.path.join(parent_directory, '\\data\\player\\players.json')
#print(parent_directory)



class Controleur:
    def __init__(self):
        self.joueurs = DAO.charger_file("players.json") or []
        self.tournois = DAO.charger_file("tournois.json") or []
        
    def addplayer(self):
        infos = View.menu_creation_joueur()
        identifiant = infos[0]
        if identifiant in self.joueurs:
            print ("Joueur déjà enregistré")
        else:
            try:
                joueur = Player(*infos)
                self.joueurs[identifiant] = joueur.to_dict()
                DAO.sauvegarder_file("players.json", self.joueurs)
                print("Joueur enregistré")
            except ValueError as e:
                print(f"{e}")
        
    def afficher_liste_player(self):
        data = self.joueurs
        data = [v for v in data.values()]
        sorted_data = sorted(data, key=itemgetter('Surname'))
        return tabulate(sorted_data, headers="keys", tablefmt="grid")
            
    def creer_tournoi(self):
        infos = View.menu_creation_tournoi()
        try :
            tournoi = Tournoi(*infos)
            self.tournois = tournoi.to_dict()
            DAO.sauvegarder_file("tournois.json", self.tournois)
            print("Tournoi enregistré")
        except ValueError as e:
            print(f"{e}")
        
    def afficher_liste_tournoi(self):
        data = self.tournois
        data = [
            {"name" : data["name"],
             "Date_debut": data["start_date"],
             "Date_fin" : data["end_date"]
            }
            for data in data.values()]
        sorted_data = sorted(data, key=itemgetter("name"))
        return tabulate(sorted_data, headers="keys", tablefmt="grid")
    
    
#print(Controleur.__init__())