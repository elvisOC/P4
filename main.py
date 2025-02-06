from controleur.controller import Controleur
from vue.view import View
import pathlib
import os
import json

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
                choix = View.menu_continuer_tournoi()
                if choix.lower() == "y":
                    print(View.menu_tournoi_ID())
                elif choix.lower() == "n":
                    controleur.afficher_liste_tournoi()
                    print(View.menu_tournoi_ID())
                    
            if second_choix == "3":
                controleur.afficher_liste_tournoi()
        elif choix == "2":
            second_choix = View.menu_joueur()
            if second_choix == "1":
                print(controleur.addplayer())
            elif second_choix == "2":
                print(controleur.afficher_liste_player())
            elif second_choix == "3":
                break
                    
        elif choix == "3":
            choix = View.menu_rapport()
            
        elif choix == "4":
            choix = View.menu_quitter()
            break

main()
