from P4.modeles.models import Player
from P4.vue.view import View
import json
import os
import pandas as pd
import pathlib
from operator import itemgetter
from tabulate import tabulate

parent_directory = pathlib.Path(__file__).parent.resolve()
directory = os.path.expandvars(fr'C:\Users\%username%\Desktop\openclassrooms\P4\data\player')
file_path = os.path.join(directory, 'players.json')

class Controleur:
    def __init__(self):
        self.joueurs = 

    def verifie_file(self):
        if os.path.exists(self.file_path) and os.path.getsize(self.file_path) > 0:
            with open (self.file_path, 'r', encoding='utf-8') as file:
                try: 
                    return json.load(file)
                except json.JSONDecodeError:
                    return True
        else:
            return {}
        
    def verifie_doublon(self):
        data = self.verifie_file()
        for player in data.values():
            if player.get('ID') == self.national_id:
                return True
            return False
        
    def addplayer(self):
        if self.verifie_file():
            return "Problème avec le fichier"
        if self.verifie_doublon():
            return f"Le joueur {self.surname} {self.name} existe déjà"
        max_id = max(map(int, data.keys())) if data else 0
        new_player_id = max_id + 1
        data[str(new_player_id)] = {
            'name' : self.name, 
            'surname' : self.surname, 
            'birthdate' : self.birthdate
            }
        with open (file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
            return f"Joueur {self.name} {self.surname} ajouté"
        
    def afficher_liste_player(self):
        if not os.path.exists(self.file_path):
            return "Fichier inexistant"
        if os.path.getsize(self.file_path) < 0:
            return "Fichier vide"
        with open (self.file_path, 'r', encoding='utf-8') as file:
            try: 
                data = json.load(file)
                data_list = [v for v in data.values()]
                sorted_data = sorted(data_list, key=itemgetter('name'))
                return tabulate(sorted_data, headers="keys", tablefmt="grid")
            except json.JSONDecodeError:
                return "Problème avec le fichier"
            
            
    def creer_tournoi(self):
        infos = View.menu_tournoi()
        
        
        
new_player = Player(national_id='AC12345', name='test', surname='moi', birthdate='31-07-1994', file_path=file_path)
result = new_player.afficher_liste_player()
print(result)