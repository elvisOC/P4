from P4.controleur.controller import Controleur
from P4.vue.view import View


def main():
    controleur= Controleur()
    while True:
        choix = View.home_menu()
        if choix == "1":
            controleur.creer_tournoi