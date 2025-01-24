import json
import os
import pandas as pd
import pathlib
from operator import itemgetter
from tabulate import tabulate
from P4.controleur.controller import Controleur

class View:

    def home_menu():
        print("1.Tournoi")
        print("2.Joueurs")
        print("3.Rapport")
        print("4.Quitter")
        return input("Choississez un menu : ")
    
    def menu_tournoi():
        print("1.Créer tournoi")
        print("2.Consulter anciens tournois")
        print("3.Revenir au menu principal")
        
    def menu_joueur():
        print("1.Ajouter joueur")
        print("2.Afficher la liste des joueurs")
        print("3.Revenir au menu principal")
        
    def menu_rapport():
        print("1.Afficher rapport")
        print("2.Revenir au menu principal")
        
    def menu_creation_joueur():
        nom = input("Nom : ")
        prenom = input("Prenom : ")
        birthdate = input("Date de naissance : ")
        identifiant = input("Identifiant : ")
        return nom, prenom, birthdate, identifiant
    
    def creer_tournoi():
        nom = input("Nom du tournoi : ")
        lieu = input("Lieu du tournoi : ")
        date_debut = input("Date de début : ")
        date_fin = input("Date de fin : ")
        nb_tour = input("Nombre de tours")
        tour_actuel = 0
        