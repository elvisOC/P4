from modeles.models import Player, Tournoi, DAO
from vue.view import View
import os
import pathlib
from operator import itemgetter
from tabulate import tabulate
import pandas
import json
import random
from datetime import datetime


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
                max_id = [int(key) for key in self.joueurs.keys() if key.isdigit()]
                new_player_id = str(max(max_id) + 1) if max_id else "1"
                joueur = Player(*infos)
                self.joueurs[new_player_id] = joueur.to_dict()
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
            max_id = [int(key) for key in self.tournois.keys() if key.isdigit()]
            new_tournament_id = str(max(max_id) + 1) if max_id else "1"
            infos = list(infos)
            list_id = infos[-1]
            name_list = [{"ID": player_id, "Name": self.return_name(player_id), "points": 0.0} for player_id in list_id]
            infos.append([])
            tournoi = Tournoi(*infos)
            nbr_matchs = len(list_id) // 2
            list_match = []
            copy_list = name_list[:]
            random.shuffle(copy_list)
            for nbr in range(nbr_matchs):
                player1 = copy_list.pop(0)["Name"]
                player2 = copy_list.pop(0)["Name"]
                list_match.append([[player1, 0.0], [player2, 0.0]])
            round_data = [{
                "name" : f"Round 1",
                "start_time": 1,
                "end_time": 1,
                "matches": list_match
                }]
            self.tournois[new_tournament_id] = tournoi.to_dict()
            self.tournois[new_tournament_id]["players"] = name_list
            self.tournois[new_tournament_id]["rounds"] = round_data
            self.tournois[new_tournament_id]["current_round"] = 1
            DAO.sauvegarder_file("tournois.json", self.tournois)
            print("Tournoi enregistré")
        except ValueError as e:
            print(f"{e}")
        
    def afficher_liste_tournoi(self):
        data = self.tournois
        data = [
            {"ID" : key,
             "name" : tournoi["name"],
             "Date_debut": tournoi["start_date"],
             "Date_fin" : tournoi["end_date"]
            }
            for key, tournoi in data.items()]
        sorted_data = sorted(data, key=itemgetter("name"))
        print(tabulate(sorted_data, headers="keys", tablefmt="grid"))
    
    def return_name(self, player_id):
        for player_key, player in self.joueurs.items():
            if player["ID"] == player_id:
                name = player.get("Name")
                surname = player.get("Surname")
                return f"{name} {surname}"
        return ("Aucun joueur trouvé avec cette ID")

        
    def creer_round(self, tournoi_id):
        tournois = self.tournois
        tournoi = tournois.get(str(tournoi_id))
        nbr_rounds = tournoi["number_of_rounds"]
        current_round = tournoi["current_round"]
        list_players = tournoi["players"]
        previous_matches = set()
        list_players.sort(key=lambda x: x[1], reverse=True)
        list_match = []
        paired = set()
        
        while len(paired) < len(list_players):
            for i in range(len(list_players)):
                if list_players[i][0] in paired:
                    continue
                for j in range(i + 1, len(list_players)):
                    if list_players[j][0] in paired:
                        continue
                    if (list_players[i][0], list_players[j][0]) not in previous_matches and \
                    (list_players[j][0], list_players[i][0]) not in previous_matches:
                        list_match.append([[list_players[i][0], 0.0], [list_players[j][0], 0.0]])
                        paired.add(list_players[i][0])
                        paired.add(list_players[j][0])
                        previous_matches.add((list_players[i][0], list_players[j][0]))
                        break


    def afficher_current_tournoi(self, tournoi_id):
        tournois = self.tournois
        tournoi = tournois.get(str(tournoi_id))
        return tournoi
            
            
    def afficher_liste_rounds(self, tournoi_id):
        data = self.tournois.get(str(tournoi_id))
        rounds = data["rounds"]
        table = []
        for round_index, round_info in enumerate(rounds, start=1):
            row = [f"Round {round_index}"] + [f"{match[0][0]} ({match[0][1]}) vs {match[1][0]} ({match[1][1]})" for match in round_info["matches"]]
            table.append(row)
        headers = ["Round"] + [f"Match {i+1}" for i in range(len(rounds[0]["matches"]))] if rounds else ["Round"]
        print(tabulate(table, headers=headers, tablefmt="grid"))
            
    def ajouter_points(self, tournoi_id):
        tournoi = self.tournois.get(str(tournoi_id))
        rounds = tournoi.get("rounds, []")
        round = rounds["rounds"]
        