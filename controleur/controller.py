from modeles.models import Player, Tournoi, DAO
from vue.view import View
import pathlib
from operator import itemgetter
from tabulate import tabulate
import random
from datetime import datetime


actual_directory = pathlib.Path(__file__).parent.resolve()
directory = actual_directory.parent


class Controleur:
    def __init__(self):
        self.joueurs = DAO.charger_file("players.json") or {}
        self.tournois = DAO.charger_file("tournois.json") or {}
        self.vue = View

    def addplayer(self):
        infos = self.vue.menu_creation_joueur()
        identifiant = infos[0]
        if identifiant in self.joueurs:
            self.vue.register_player()
        else:
            try:
                max_id = [int(key) for key in self.joueurs.keys() if key.isdigit()]
                new_player_id = str(max(max_id) + 1) if max_id else "1"
                joueur = Player(*infos)
                self.joueurs[new_player_id] = joueur.to_dict()
                DAO.sauvegarder_file("players.json", self.joueurs)
                self.vue.register_player()
            except ValueError as e:
                self.vue.afficher_message(e)

    def afficher_liste_player(self):
        data = self.joueurs
        data = [v for v in data.values()]
        sorted_data = sorted(data, key=itemgetter('Surname'))
        self.vue.print_table(sorted_data, "keys")

    def creer_tournoi(self):
        infos = self.vue.menu_creation_tournoi()
        try:
            if not isinstance(self.tournois, dict):
                self.tournois = {}
            if not self.tournois:
                new_tournament_id = "1"
            else:
                max_id = max((int(key) for key in self.tournois.keys() if key.isdigit()), default=0)
                new_tournament_id = str(max_id + 1)
            infos = list(infos)
            list_id = infos[-1]
            name_list = [{"ID": player_id, "Name": self.return_name(player_id), "points": 0.0} for player_id in list_id]
            infos.append([])
            tournoi = Tournoi(*infos)
            nbr_matchs = len(list_id) // 2
            list_match = []
            copy_list = name_list[:]
            random.shuffle(copy_list)
            for _ in range(nbr_matchs):
                player1 = copy_list.pop(0)["Name"]
                player2 = copy_list.pop(0)["Name"]
                list_match.append([[player1, 0.0], [player2, 0.0]])
            round_data = [{
                "name": "Round 1",
                "start_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "end_time": None,
                "matches": list_match
            }]
            self.tournois[new_tournament_id] = tournoi.to_dict()
            self.tournois[new_tournament_id]["players"] = name_list
            self.tournois[new_tournament_id]["rounds"] = round_data
            self.tournois[new_tournament_id]["current_round"] = 1
            DAO.sauvegarder_file("tournois.json", self.tournois)
            self.vue.afficher_message("Tournoi enregistré avec succès.")
            self.afficher_liste_match(new_tournament_id, 0)
        except ValueError as e:
            self.vue.afficher_message(f"Erreur lors de la création du tournoi : {e}")

    def afficher_liste_tournoi(self):
        data = self.tournois
        data = [
            {"ID": key,
             "name": tournoi["name"],
             "Date_debut": tournoi["start_date"],
             "Date_fin": tournoi["end_date"],
             "Nombre de rounds": tournoi["number_of_rounds"],
             "Tour actuel": tournoi["current_round"]
            }
            for key, tournoi in data.items()]
        sorted_data = sorted(data, key=lambda x: int(x["ID"]))
        self.vue.print_table(sorted_data, "keys")

    def return_name(self, player_id):
        for player_key, player in self.joueurs.items():
            if player["ID"] == player_id:
                name = player.get("Name")
                surname = player.get("Surname")
                return f"{name} {surname}"
        return ("Aucun joueur trouvé avec cette ID")

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
        self.vue.print_table(table, headers)

    def afficher_liste_match(self, tournoi_id, round_id):
        data = self.tournois.get(str(tournoi_id))
        round_id = int(round_id) - 1
        matchs = data["rounds"][round_id]["matches"]
        match_list = [
            [i, match[0][0], match[0][1], match[1][0], match[1][1]]
            for i, match in enumerate(matchs, start=1)
        ]
        headers = ["Match", "Joueur 1", "Score 1", "Joueur 2", "Score 2"]
        self.vue.print_table(match_list, headers)

    def afficher_match(self, tournoi_id, round_id, match_id):
        data = self.tournois.get(str(tournoi_id))
        round_id = int(round_id) - 1
        match_id = int(match_id) - 1
        match = data["rounds"][round_id]["matches"][match_id]
        match_data = [
            [match[0][0], match[0][1]], [match[1][0], match[1][1]]]
        headers=["Joueur", "Score"]
        self.vue.print_table(match_data, headers)
        if match[0][1] == 0.0 and match[1][1] == 0.0:
            resultat = self.vue.resultat()
            self.ajouter_score(tournoi_id, round_id, match_id, resultat)

    def ajouter_score(self, tournoi_id, round_id, match_id, resultat):
        data = self.tournois.get(str(tournoi_id))
        match = data["rounds"][round_id]["matches"][match_id]
        resultat = int(resultat)
        joueurs = {joueur["Name"]: joueur for joueur in data["players"]}
        if resultat == 1:
            match[0][1] += 1
            match[1][1] += 0
        elif resultat == 2:
            match[0][1] += 0
            match[1][1] += 1
        elif resultat == 3:
            match[0][1] += 0.5
            match[1][1] += 0.5
        else:
            self.vue.afficher_message("Erreur : Valeur invalide pour vainqueur. Utilisez 1, 2 ou 3.")
        if match[0][0] in joueurs:
            joueurs[match[0][0]]["points"] += match[0][1]
        if match[1][0] in joueurs:
            joueurs[match[1][0]]["points"] += match[1][1]
        data["rounds"][round_id]["matches"][match_id] = match
        self.tournois[str(tournoi_id)] = data
        DAO.sauvegarder_file("tournois.json", self.tournois)
        self.verifier_round_fini(tournoi_id, round_id)
        self.afficher_liste_match(tournoi_id, round_id)

    def verifier_round_fini(self, tournoi_id, round_id):
        data = self.tournois.get(str(tournoi_id))
        round_actuel = data["rounds"][round_id]
        for match in round_actuel["matches"]:
            if match[0][1] == 0.0 and match[1][1] == 0.0:
                return 1
            elif round_actuel["end_time"] is not None:
                return
        confirmation = input(f"Voulez-vous clôturer {round_actuel['name']} ? (oui/non) ").strip().lower()
        if confirmation != "oui":
            self.vue.afficher_message("Le round n'a pas été clôturé.")
            return
        round_actuel["end_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.vue.round_fini(round_actuel['name'], round_actuel['end_time'])
        data["rounds"][round_id] = round_actuel
        data["current_round"] = round_id + 1
        self.tournois[str(tournoi_id)] = data
        DAO.sauvegarder_file("tournois.json", self.tournois)
        if round_id + 1 < data["number_of_rounds"]:
            creer_nouveau = self.vue.next_round()
            if creer_nouveau == "oui":
                quand = self.vue.start_now()
                if quand == "oui":
                    self.creer_nouveau_round(tournoi_id, round_id + 1, datetime.now().strftime("%d-%M-%Y %H:%M"))
                else:
                    date_heure = self.vue.when
                    self.creer_nouveau_round(tournoi_id, round_id, date_heure)
            else:
                self.vue.afficher_message("Le tournoi reste sur ce round.")
        else:
            self.vue.afficher_message("Le tournoi est terminé !")

    def creer_nouveau_round(self, tournoi_id, round_id, date):
        data = self.tournois.get(str(tournoi_id))
        joueurs = data["players"]
        joueurs = sorted(joueurs, key=lambda x: x["points"], reverse=True)
        historique_matchs = set()
        for round_data in data["rounds"]:
            for match in round_data["matches"]:
                joueur1, joueur2 = match[0][0], match[1][0]
                historique_matchs.add(frozenset([joueur1, joueur2]))
        matches = []
        joueurs_restants = joueurs.copy()
        while joueurs_restants:
            joueur1 = joueurs_restants.pop(0)
            for i, joueur2 in enumerate(joueurs_restants):
                if frozenset([joueur1["Name"], joueur2["Name"]]) not in historique_matchs:
                    matches.append([[joueur1["Name"], 0.0], [joueur2["Name"], 0.0]])
                    joueurs_restants.pop(i)
                    break
        nouveau_round = {
            "name": f"Round {round_id + 1}",
            "start_time": date,
            "end_time": None,
            "matches": matches
        }
        data["rounds"].append(nouveau_round)
        data["current_round"] = round_id + 1
        self.tournois[str(tournoi_id)] = data
        DAO.sauvegarder_file("tournois.json", self.tournois)
