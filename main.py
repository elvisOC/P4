from controleur.controller import Controleur
from vue.view import View
from modeles.models import DAO
import pathlib
import os

directory = pathlib.Path(__file__).parent.resolve()
player_path = os.path.join(directory, 'data\\players.json')


def main():
    controleur = Controleur()
    while True:
        choix = View.home_menu()
        if choix == "1":
            second_choix = View.menu_tournoi()
            if second_choix == "1":
                controleur.creer_tournoi()
            if second_choix == "2":
                controleur.afficher_liste_tournoi()
                tournoi_id = View.menu_tournoi_ID()
                if tournoi_id.strip().lower() == "q":
                    continue
                controleur.afficher_liste_rounds(tournoi_id)
                round_id = View.menu_rounds()
                if round_id.strip().lower() == "q":
                    continue
                controleur.afficher_liste_match(tournoi_id, round_id)
                while controleur.verifier_round_fini(tournoi_id, int(round_id) - 1) == 1:
                    match_id = View.menu_matchs()
                    controleur.afficher_match(tournoi_id, round_id, match_id)
                    data = DAO.charger_file("tournois.json")
                    tournoi = data.get(str(tournoi_id))
                    round = tournoi["rounds"][int(round_id) - 1]
                    if round["end_time"] is not None:
                        break
                    elif match_id.strip().lower() == "q":
                        continue

        elif choix == "2":
            second_choix = View.menu_joueur()
            if second_choix == "1":
                print(controleur.addplayer())
            elif second_choix == "2":
                print(controleur.afficher_liste_player())
            elif second_choix == "3":
                break

        elif choix == "3":
            choix = View.menu_quitter()
            break


main()
