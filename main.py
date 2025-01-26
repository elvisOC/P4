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
                    
        elif choix == "2":
            second_choix = View.menu_joueur()
            if second_choix == "1":
                print(controleur.addplayer())
            elif second_choix == "2":
                print(controleur.afficher_liste_player(player_path))
            elif second_choix == "3":
                break
                    
        elif choix == "3":
            choix = View.menu_rapport()
            
        elif choix == "4":
            choix = View.menu_quitter()
            break

main()
